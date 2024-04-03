import streamlit as st
import pandas as pd

# Sample data for the table
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Organization': ['ABC Inc.', 'XYZ Corp.', '123 Industries', 'Tech Solutions'],
    'Room Number': [101, 205, 307, 410]
}
df = pd.DataFrame(data)

# Function to filter data based on search input
def filter_data(df, query):
    return df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().values, axis=1)]

# Main function to run the Streamlit app
def main():
    st.title('Search Results')
    
    # Search input box
    search_query = st.text_input('Search:', '')
    
    # Submit button
    if st.button('Submit'):
        # Filter data based on search query
        filtered_df = filter_data(df, search_query)
        
        # Display search results
        if not filtered_df.empty:
            st.write(filtered_df)
        else:
            st.write('No results found.')
        
        # Clear search query after submission
        search_query = ''

if __name__ == "__main__":
    main()
