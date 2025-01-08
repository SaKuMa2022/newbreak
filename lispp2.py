import streamlit as st
import pandas as pd
from openpyxl import load_workbook

# Define the Excel file path
excel_file = 'students_data.xlsx'

# Function to load existing data from the Excel file or create a new one if it doesn't exist
def load_or_create_data():
    try:
        # Load the existing Excel file
        wb = load_workbook(excel_file)
        sheet = wb.active
        data = pd.DataFrame(sheet.values)
        data.columns = ["Student Name", "Student ID", "Age", "Sex", "Subject 1", "Subject 2", "Subject 3", "Subject 4"]
        return data
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        return pd.DataFrame(columns=["Student Name", "Student ID", "Age", "Sex", "Subject 1", "Subject 2", "Subject 3", "Subject 4"])

# Function to save data to the Excel file
def save_data_to_excel(df):
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Students")

# Main app code
def main():
    st.title("Student Data Form")

    # Create input fields
    student_name = st.text_input("Student Name")
    student_id = st.text_input("Student ID")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    subject_1 = st.number_input("Grade for Subject 1", min_value=0, max_value=100, step=1)
    subject_2 = st.number_input("Grade for Subject 2", min_value=0, max_value=100, step=1)
    subject_3 = st.number_input("Grade for Subject 3", min_value=0, max_value=100, step=1)
    subject_4 = st.number_input("Grade for Subject 4", min_value=0, max_value=100, step=1)

    # Load existing data
    df = load_or_create_data()

    # On submit button click
    if st.button("Submit"):
        # Collect the data into a new row
        new_data = {
            "Student Name": student_name,
            "Student ID": student_id,
            "Age": age,
            "Sex": sex,
            "Subject 1": subject_1,
            "Subject 2": subject_2,
            "Subject 3": subject_3,
            "Subject 4": subject_4
        }
        
        # Append the new row to the DataFrame
        df = df.append(new_data, ignore_index=True)

        # Save updated data to Excel
        save_data_to_excel(df)

        # Show the updated table
        st.subheader("Updated Student Data")
        st.write(df)

        # Clear input fields
        st.experimental_rerun()

#if __name__ == "__main__":
    main()
