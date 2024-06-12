import streamlit as st
import pandas as pd

@ st.cache_data

def load_data():
    return pd.read_csv(r'antidata_6.12.csv', encoding= 'unicode_escape')

df=load_data()

#print(df.head())

df.rename(columns={'ï»¿DRUG NAME':'Antibiotic','Organism/Organism Group':'Organism' },inplace=True)

#print(df.columns)

def filter_dataframe(query):
    return df[df['Antibiotic'].str.contains(query,case=False) |
              df['Organism'].str.contains(query,case=False)]


    




#Streamlit app
 
def main():
    st.title(':red[MICfinder   v1.0]')
    st.subheader(':violet[(Gram-negative and Gram-positive bacteria)]')
    st.markdown(''':green[Infectious disease professionals and researchers require antibacterial
                susceptibility testing results to determine if an antibacterial is potentially useful in the
                treatment of bacterial infection. MIC is critical in that regard.
                Breakpoint setting requires integration of knowledge wild type distribution of MICs and other
                factors(doi:10.1128/CMR.0047-06.) ]''')

    st.markdown(':blue-background[Please type in a few letters of  either antibiotic or organism and press enter]')
    st.text('Please use the refresh button on your browser to clear search results')
    


    antib_search = st.text_input('Search by Antibiotic:','', key='antib_search')
    antib_suggestions= df['Antibiotic'].unique().tolist()


    org_search = st.text_input('Search by Organism:', '', key='org_search')
    org_suggestions = df['Organism'].unique().tolist()


    if antib_search or  org_search:
        filtered_df = filter_dataframe(antib_search) if antib_search else filter_dataframe(org_search)

        st.write(filtered_df)
    else:
        st.write(' Enter a valid query.')

    antib_search = ' '
    org_search = ' '    

if __name__ =="__main__":
    main()    


