import streamlit as st
import numpy as np
from joblib import load

# Load Model
model = load('./employee_salary_model.joblib')

st.title("Employee Salary Prediction App")
st.write("Predict employee salary based on years of experience")

# User Input
experience = st.number_input("Enter Years of Experience:", min_value=0, max_value=30, step=1)

if st.button("Predict"):
    if experience == 0:
        st.warning("Please enter a valid number of years")
    else:
        salary = model.predict(np.array([[experience]]))
        st.success(f"The Predicted Salary is: {salary[0]:,.2f} EGP")
