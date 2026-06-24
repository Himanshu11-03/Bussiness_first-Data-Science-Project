import streamlit as st
import pickle
import numpy as np

model = pickle.load(
    open(
        "attrition_model.pkl",
        "rb"
    )
)

st.title("Employee Attrition Prediction")

age = st.number_input("Age", 18, 60)

income = st.number_input(
    "Monthly Income",
    1000,
    50000
)

years = st.number_input(
    "Years At Company",
    0,
    40
)

overtime = st.selectbox(
    "OverTime",
    ["No","Yes"]
)

overtime = 1 if overtime=="Yes" else 0

if st.button("Predict"):
    # 1. Combine your inputs into a 2D array/list
    # You would need to provide the expected number of elements
    sample = np.array([[age, income, years, overtime, default_val5, default_val6, ...]])
    
    # 2. Make the prediction
    prediction = model.predict(sample)
    
    # 3. Display the result
    if prediction[0] == 1:
        st.error("The employee is likely to leave.")
    else:
        st.success("The employee is likely to stay.")
