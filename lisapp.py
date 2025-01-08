import streamlit as st
import pandas as pd
import os
from openpyxl.workbook import workbook

# Path for the Excel file
EXCEL_FILE = "student_data.xlsx"

# Streamlit app title
st.title("Student Data Input Form")

# Define the form using Streamlit widgets
with st.form(key='student_form'):
    student_name = st.text_input("Student Name")
    student_id = st.text_input("Student ID")
    student_age = st.number_input("Student Age", min_value=1, max_value=100)
    sex = st.radio("Student Sex", ("Male", "Female"))
    
    subject_1 = st.number_input("Grade for Subject 1", min_value=0.0, max_value=100.0, step=0.1)
    subject_2 = st.number_input("Grade for Subject 2", min_value=0.0, max_value=100.0, step=0.1)
    subject_3 = st.number_input("Grade for Subject 3", min_value=0.0, max_value=100.0, step=0.1)
    subject_4 = st.number_input("Grade for Subject 4", min_value=0.0, max_value=100.0, step=0.1)
    
    # Submit button
    submit_button = st.form_submit_button("Submit")

# Handling form submission
if submit_button:
    # Check if all fields are filled
    if not (student_name and student_id and student_age and sex and subject_1 and subject_2 and subject_3 and subject_4):
        st.error("All fields must be filled!")
    else:
        # Prepare the data
        student_data = {
            'Name': student_name,
            'ID': student_id,
            'Age': student_age,
            'Sex': sex,
            'Subject 1': subject_1,
            'Subject 2': subject_2,
            'Subject 3': subject_3,
            'Subject 4': subject_4
        }

        # Create a DataFrame for the new student data
        new_data = pd.DataFrame([student_data])

        # Check if the Excel file exists, if not, create it with headers
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
            # Concatenate the new data with the existing DataFrame
            df = pd.concat([df, new_data], ignore_index=True)
        else:
            # If the file doesn't exist, create a new DataFrame
            df = new_data

        # Save to Excel file
        df.to_excel(EXCEL_FILE, index=False)

        # Show success message
        st.success(f"Student data saved for {student_name}")

        # Clear the form inputs (Streamlit automatically clears the form on re-run)

    
