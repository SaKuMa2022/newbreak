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
    st.title('Hidden Table with Search')
    
    # Search input box
    search_query = st.text_input('Search:', '')
    
    # Filter data based on search query
    filtered_df = filter_data(df, search_query)
    
    # Button to toggle table visibility
    if st.button('Toggle Table Visibility'):
        st.write(filtered_df)  # Display the table if the button is clicked
    else:
        st.write('Table is hidden.')  # Display a message when the table is hidden

if __name__ == "__main__":
    main()
