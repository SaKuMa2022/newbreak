import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Emma', 'Michael', 'Sophia'],
    'Organization': ['ABC Inc.', 'XYZ Corp.', 'LMN Ltd.', 'PQR Co.'],
    'Room Number': [101, 202, 303, 404]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to filter DataFrame based on query
def filter_data(query):
    query = query.lower()
    filtered_df = df[df['Name'].str.lower().str.contains(query) |
                     df['Organization'].str.lower().str.contains(query) |
                     df['Room Number'].astype(str).str.contains(query)]
    return filtered_df

# Streamlit app
def main():
    st.title('Employee Directory')

    # Input box for query
    query = st.text_input('Search by Name, Organization, or Room Number')

    # Filter data based on query
    filtered_data = filter_data(query)

    # Display filtered data in a table
    st.table(filtered_data)

if __name__ == "__main__":
    main()
