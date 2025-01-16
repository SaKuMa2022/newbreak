import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from google.auth import exceptions

# Function to authenticate Google API
def authenticate_google_drive():
    credentials = None
    try:
        # Define the scope and authenticate the credentials
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
        creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        client = gspread.authorize(creds)
        return client
    except exceptions.GoogleAuthError as e:
        st.error("Authentication failed: Please check the credentials and try again.")
        raise e

# Streamlit form to input student data
def student_form():
    st.title("Student Data Input Form")
    
    with st.form(key='student_form'):
        # Student Information Input Fields
        name = st.text_input("Student Name")
        student_id = st.text_input("Student ID")
        age = st.number_input("Age", min_value=1, max_value=100)
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])
        
        # Subject grades input
        subject1_grade = st.number_input("Grade for Subject 1", min_value=0, max_value=100)
        subject2_grade = st.number_input("Grade for Subject 2", min_value=0, max_value=100)
        subject3_grade = st.number_input("Grade for Subject 3", min_value=0, max_value=100)
        subject4_grade = st.number_input("Grade for Subject 4", min_value=0, max_value=100)
        
        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Create a DataFrame from the input data
            student_data = {
                "Student Name": name,
                "Student ID": student_id,
                "Age": age,
                "Sex": sex,
                "Subject 1 Grade": subject1_grade,
                "Subject 2 Grade": subject2_grade,
                "Subject 3 Grade": subject3_grade,
                "Subject 4 Grade": subject4_grade
            }

            df = pd.DataFrame([student_data])
            return df
        else:
            return None

def main():
    # Get student data from the form
    student_data = student_form()

    if student_data is not None:
        # Authenticate Google Drive and Sheets
        try:
            client = authenticate_google_drive()

            # Open or create the Google Sheet
            sheet_name = "Student Data"
            try:
                sheet = client.open(sheet_name).sheet1
            except gspread.exceptions.SpreadsheetNotFound:
                # Create a new Google Sheet if it doesn't exist
                sheet = client.create(sheet_name).sheet1
                # Add headers to the sheet if it's new
                sheet.append_row([
                    "Student Name", "Student ID", "Age", "Sex", 
                    "Subject 1 Grade", "Subject 2 Grade", 
                    "Subject 3 Grade", "Subject 4 Grade"
                ])
            
            # Append the student data to the sheet
            sheet.append_rows(student_data.values.tolist())
            st.success(f"Student data successfully added to {sheet_name}!")

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
