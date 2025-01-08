import streamlit as st
import pandas as pd
import os
from openpyxl.workbook import workbook

# Path for the Excel file
EXCEL_FILE = "patient_data.xlsx"

# Streamlit app title
st.title("Lab Data Input Form")

# Define the form using Streamlit widgets
with st.form(key='Patient_form'):
    patient_name = st.text_input("Patient Name")
    patient_id = st.text_input("MRN")
    patient_age = st.number_input("Patient Age", min_value=1, max_value=100)
    sex = st.radio("Patient Sex", ("Male", "Female"))
    
    test_1 = st.number_input("Value for test 1", min_value=0.0, max_value=100.0, step=0.1)
    test_2 = st.number_input("Value for test 2", min_value=0.0, max_value=100.0, step=0.1)
    test_3 = st.number_input("Value for test 3", min_value=0.0, max_value=100.0, step=0.1)
    test_4 = st.number_input("Value for test 4", min_value=0.0, max_value=100.0, step=0.1)
    
    # Submit button
    submit_button = st.form_submit_button("Submit")
    
 
# Handling form submission
if submit_button:
    # Check if all fields are filled
    if not (patient_name and patient_id and pateint_age and sex and test_1 and test_2 and test_3 and subject_4):
        st.error("All fields must be filled!")
    else:
        # Prepare the data
        patient_data = {
            'Name': student_name,
            'MRN': patient_id,
            'Age': patient_age,
            'Sex': sex,
            'Test 1': test_1,
            'Testt 2': test_2,
            'Test 3': test_3,
            'Test 4': test_4
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

        
