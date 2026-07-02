import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("diabetes_model.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction System")

st.write("Enter the patient's medical information below.")

st.divider()

# -----------------------------
# Input Fields
# -----------------------------

preg = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1
)

glucose = st.number_input(
    "Glucose",
    min_value=0,
    max_value=250,
    value=120
)

bp = st.number_input(
    "Blood Pressure",
    min_value=0,
    max_value=150,
    value=70
)

skin = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20
)

insulin = st.number_input(
    "Insulin",
    min_value=0,
    max_value=900,
    value=80
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=30.0
)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

st.divider()

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("Predict Diabetes"):

    data = np.array([
        [
            preg,
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]
    ])

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    confidence = np.max(probability) * 100

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("🔴 Patient is likely to have Diabetes")
    else:
        st.success("🟢 Patient is NOT Diabetic")

    st.write(f"**Confidence : {confidence:.2f}%**")

