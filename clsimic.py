import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import os

# ---------------------------------------------------------------------------
# CONFIG — fill these in once you have your accounts set up
# ---------------------------------------------------------------------------
ADSENSE_CLIENT_ID = "ca-pub-XXXXXXXXXXXXXXXX"   # from your AdSense account
ADSENSE_SLOT_ID = "XXXXXXXXXX"                   # from the specific ad unit you create
ADSENSE_VERIFICATION_SNIPPET = "<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2167773518291978"
     crossorigin="anonymous"></script>"                # paste Google's one-time site-verification <script> tag here, as a string
PLAUSIBLE_DOMAIN = "your-app-domain.streamlit.app"  # your app's public domain
ENABLE_ADS = False          # flip to True once AdSense approves your site
ENABLE_ANALYTICS = False    # flip to True once you've set up Plausible (or swap for your own)

# ---------------------------------------------------------------------------
# Data loading (unchanged)
# ---------------------------------------------------------------------------
def _inject_head_html(html_snippet, marker):
    """
    components.html() always renders inside a sandboxed iframe, which is
    invisible to crawlers (like Google's AdSense site-verification check)
    that fetch the page's real HTML source. Streamlit serves one shared
    index.html from its own installed package, so patching that file
    directly -- once, before any request is served -- gets the snippet
    into the actual <head> that Google's crawler sees.

    `marker` is a short, unique string (e.g. the ca-pub- ID) used to check
    whether the injection already happened, so re-running this on every
    app rerun doesn't duplicate it. It only needs to re-run after a fresh
    deploy, when Streamlit's own index.html is reset to its original state.
    """
    if not html_snippet:
        return
    try:
        index_path = os.path.join(os.path.dirname(st.__file__), "static", "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        if marker in content:
            return  # already injected for this deploy
        content = content.replace("</head>", html_snippet + "\n</head>")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        # Never let a failed injection break the actual tool -- ads or
        # verification just won't show if this fails for some reason.
        pass


# Run once at import time, before Streamlit serves any request, so the tag
# is already in place when Google's crawler visits the page.
if ADSENSE_VERIFICATION_SNIPPET:
    _inject_head_html(ADSENSE_VERIFICATION_SNIPPET, marker=ADSENSE_CLIENT_ID)


@st.cache_data
def load_data():
    # Try encodings in order of likelihood. utf-8-sig automatically strips a
    # UTF-8 byte-order-mark (BOM), which is what caused 'ï»¿DRUG NAME' to
    # appear instead of 'DRUG NAME' when the file was read with
    # 'unicode_escape'. latin1 is kept as a last-resort fallback for older
    # exports that used a different encoding for special characters.
    last_error = None
    for enc in ('utf-8-sig', 'utf-8', 'latin1'):
        try:
            data = pd.read_csv(r'clsi_fda_6.10.csv', encoding=enc)
            break
        except UnicodeDecodeError as e:
            last_error = e
    else:
        raise RuntimeError(f"Could not decode antimidata1.csv with any known encoding: {last_error}")

    # Strip any leftover BOM character and whitespace from headers, in case
    # a BOM slips through as a literal '\ufeff' rather than being consumed
    # by the encoding itself.
    data.columns = [c.replace('\ufeff', '').strip() for c in data.columns]
    return data

df = load_data()

# Map from a normalized (lowercase, no extra spaces) version of the expected
# header to a normalized version of each actual column, so 'DRUG NAME',
# 'Drug Name', or 'drug name ' all match the same target. Both
# 'Organism/Organism Group' and a plain 'Organism' column are accepted,
# since different CSV exports have used either.
_rename_map = {}
_targets = {
    'drug name': 'Antibiotic',
    'organism/organism group': 'Organism',
    'organism': 'Organism',
}
for col in df.columns:
    key = col.strip().lower()
    if key in _targets:
        _rename_map[col] = _targets[key]
df.rename(columns=_rename_map, inplace=True)

# Fail loudly and clearly instead of a cryptic KeyError three lines later.
_missing = [target for target in _targets.values() if target not in df.columns]
if _missing:
    st.error(
        f"The CSV is missing expected column(s): {', '.join(_missing)}. "
        f"Actual columns found in the file: {list(df.columns)}. "
        "Check the new CSV's header row for a renamed or differently "
        "formatted column and update the app's column mapping to match."
    )
    st.stop()


def filter_dataframe(query):
    return df[df['Antibiotic'].str.contains(query, case=False) |
              df['Organism'].str.contains(query, case=False)]


# ---------------------------------------------------------------------------
# Ad + analytics helpers
# ---------------------------------------------------------------------------
def render_ad_slot():
    """Renders a single AdSense display ad. Safe no-op if ENABLE_ADS is False."""
    if not ENABLE_ADS:
        return
    ad_html = f"""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT_ID}"
     crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="{ADSENSE_CLIENT_ID}"
         data-ad-slot="{ADSENSE_SLOT_ID}"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({{}});
    </script>
    """
    components.html(ad_html, height=120)


def inject_analytics():
    """Injects the Plausible analytics script into the page head. Safe no-op if disabled."""
    if not ENABLE_ANALYTICS:
        return
    analytics_html = f"""
    <script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>
    """
    components.html(analytics_html, height=0)


def log_search_event(query_type, query_value):
    """
    Very lightweight server-side event log. This is optional and separate from
    Plausible (which only sees pageviews, not what was searched). Swap the body
    of this function for a call to your own logging endpoint, a Google Sheet,
    or a small database (e.g. Supabase) if you want to know which
    antibiotic/organism lookups are most common.
    """
    if not ENABLE_ANALYTICS:
        return
    try:
        # Placeholder — replace with a real logging endpoint you control.
        # Left as a no-op so the app doesn't break before you wire one up.
        pass
    except Exception:
        # Never let logging failures break the actual tool.
        pass


# ---------------------------------------------------------------------------
# Streamlit app
# ---------------------------------------------------------------------------
def main():
    inject_analytics()

    st.title(':red[MICfinder v1.0]')
    st.subheader(':violet[(Gram-negative and Gram-positive bacteria)]')
    st.markdown(''':green[Infectious disease professionals and researchers require antibacterial
    susceptibility testing results to determine if an antibacterial is potentially useful in the
    treatment of bacterial infection. MIC(values in µg/ml) is critical in that regard.
    Breakpoint setting requires integration of knowledge of wild type distribution of MICs and other
    factors(doi:10.1128/CMR.0047-06.) ]''')
    st.markdown(':blue-background[Please type in a few letters of either antibiotic or organism and press enter(return/done on mobile devices keyboard)]')
    st.text('Please use the refresh button on your browser to clear search results')

    # Top ad slot — sits above the search inputs, doesn't interrupt the tool itself
    render_ad_slot()

    antib_search = st.text_input('Search by Antibiotic:', '', key='antib_search')
    org_search = st.text_input('Search by Organism:', '', key='org_search')

    if antib_search or org_search:
        query = antib_search if antib_search else org_search
        filtered_df = filter_dataframe(query)
        log_search_event('antibiotic' if antib_search else 'organism', query)
        st.write(filtered_df)

        # Second ad slot below results — this is where most engaged users will look
        render_ad_slot()
    else:
        st.write('Enter a valid query.')


if __name__ == "__main__":
    main()
