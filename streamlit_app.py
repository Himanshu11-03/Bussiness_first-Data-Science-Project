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

    sample = np.array([
        [age,
         income,
         years,
         overtime]
    ])

    prediction = model.predict(sample)

    if prediction[0]==1:
        st.error(
            "Employee may leave."
        )
    else:
        st.success(
            "Employee likely to stay."
        )