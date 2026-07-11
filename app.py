import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

st.title("Student Marks Predictor")

hours = st.number_input("Enter study hours", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Predict"):
    prediction = model.predict(pd.DataFrame([[hours]], columns=["Hours"]))
    st.success(f"Predicted Marks: {prediction[0]:.2f}")