import streamlit as st
import pandas as pd

# Streamlit app layout
st.title("Student Information Input Form")

# Create form for student details
with st.form(key='student_form'):
    student_name = st.text_input("Name")
    student_id = st.text_input("Student ID")
    student_age = st.number_input("Age", min_value=1, max_value=100)
    student_sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    
    # Input grades for 4 subjects
    subject1 = st.number_input("Grade for Subject 1", min_value=0, max_value=100)
    subject2 = st.number_input("Grade for Subject 2", min_value=0, max_value=100)
    subject3 = st.number_input("Grade for Subject 3", min_value=0, max_value=100)
    subject4 = st.number_input("Grade for Subject 4", min_value=0, max_value=100)

    # Submit button
    submit_button = st.form_submit_button("Submit")

# After form submission
if submit_button:
    # Create a DataFrame to display the submitted data
    student_data = {
        "Student Name": [student_name],
        "Student ID": [student_id],
        "Age": [student_age],
        "Sex": [student_sex],
        "Subject 1": [subject1],
        "Subject 2": [subject2],
        "Subject 3": [subject3],
        "Subject 4": [subject4]
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(student_data)
    
    # Display the data in a table
    st.write("Submitted Student Data:")
    st.table(df)
    
    # Reset inputs after submission
    st.experimental_rerun()
