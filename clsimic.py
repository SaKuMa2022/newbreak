import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# CONFIG — fill these in once you have your accounts set up
# ---------------------------------------------------------------------------
ADSENSE_CLIENT_ID = "ca-pub-XXXXXXXXXXXXXXXX"   # from your AdSense account
ADSENSE_SLOT_ID = "XXXXXXXXXX"                   # from the specific ad unit you create
PLAUSIBLE_DOMAIN = "your-app-domain.streamlit.app"  # your app's public domain
ENABLE_ADS = False          # flip to True once AdSense approves your site
ENABLE_ANALYTICS = False    # flip to True once you've set up Plausible (or swap for your own)

# ---------------------------------------------------------------------------
# Data loading (unchanged)
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    data = pd.read_csv(r'clsi_fda_6.10.csv', encoding='unicode_escape')
    # Normalize headers defensively: strip whitespace and collapse case/spacing
    # differences so a re-exported CSV with slightly different header
    # formatting doesn't silently break the rename below.
    data.columns = [c.strip() for c in data.columns]
    return data

df = load_data()

# Map from a normalized (lowercase, no extra spaces) version of the expected
# header to a normalized version of each actual column, so 'DRUG NAME',
# 'Drug Name', or 'drug name ' all match the same target.
_rename_map = {}
_targets = {'drug name': 'Antibiotic', 'organism/organism group': 'Organism'}
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
