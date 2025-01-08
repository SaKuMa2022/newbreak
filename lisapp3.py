import streamlit as st
import pandas as pd

# Initialize session state to store student data across form submissions
if 'student_data' not in st.session_state:
    st.session_state.student_data = []

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
    # Store the new student data in a dictionary
    student_entry = {
        "Student Name": student_name,
        "Student ID": student_id,
        "Age": student_age,
        "Sex": student_sex,
        "Subject 1": subject1,
        "Subject 2": subject2,
        "Subject 3": subject3,
        "Subject 4": subject4
    }
    
    # Append the new entry to the session state list
    st.session_state.student_data.append(student_entry)
    
    # Clear the form fields by rerunning the script
    #st.experimental_rerun()

# Display the table of all submitted student data
if len(st.session_state.student_data) > 0:
    df = pd.DataFrame(st.session_state.student_data)
    st.write("All Submitted Student Data:")
    st.table(df)
