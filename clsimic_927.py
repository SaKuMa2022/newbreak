import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
PLAUSIBLE_DOMAIN = "your-app-domain.streamlit.app"  # your app's public domain
ENABLE_ANALYTICS = False    # flip to True once you've set up Plausible (or swap for your own)

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
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


def filter_dataframe(antibiotic_query, organism_query):
    """
    Filters on whichever fields are non-empty, combined with AND, so
    entering both an antibiotic and an organism narrows the result to rows
    matching both, rather than matching either one alone.
    """
    result = df
    if antibiotic_query:
        result = result[result['Antibiotic'].str.contains(antibiotic_query, case=False, na=False)]
    if organism_query:
        result = result[result['Organism'].str.contains(organism_query, case=False, na=False)]
    return result


# ---------------------------------------------------------------------------
# Analytics helper
# ---------------------------------------------------------------------------
def inject_analytics():
    """Injects the Plausible analytics script into the page. Safe no-op if disabled."""
    if not ENABLE_ANALYTICS:
        return
    import streamlit.components.v1 as components
    analytics_html = f"""
    <script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>
    """
    components.html(analytics_html, height=0)


def log_search_event(antibiotic_query, organism_query):
    """
    Very lightweight server-side event log. Swap the body of this function
    for a call to your own logging endpoint, a Google Sheet, or a small
    database (e.g. Supabase) if you want to know which antibiotic/organism
    lookups are most common.
    """
    if not ENABLE_ANALYTICS:
        return
    try:
        # Placeholder — replace with a real logging endpoint you control.
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
    st.markdown(':blue-background[Enter a few letters of an antibiotic, an organism, or both to narrow your results, then press enter (return/done on mobile keyboards)]')
    st.text('Please use the refresh button on your browser to clear search results')

    antib_search = st.text_input('Search by Antibiotic:', '', key='antib_search')
    org_search = st.text_input('Search by Organism:', '', key='org_search')

    if antib_search or org_search:
        filtered_df = filter_dataframe(antib_search, org_search)
        log_search_event(antib_search, org_search)
        st.write(filtered_df)
    else:
        st.write('Enter a valid query.')


if __name__ == "__main__":
    main()
