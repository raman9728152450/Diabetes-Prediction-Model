# 🩺 Diabetes Prediction Model

A machine learning web app that predicts whether a patient is likely to have diabetes, based on key diagnostic measurements. The app is built with **Streamlit** and served through a trained scikit-learn model.

## Overview

This project trains a classification model on the Pima Indians Diabetes dataset and wraps it in a simple, interactive Streamlit interface. Users enter a patient's medical details and get an instant prediction along with a confidence score.

## Features

- Interactive web form for entering patient data
- Instant diabetes prediction (Diabetic / Not Diabetic)
- Prediction confidence percentage
- Clean, centered UI built with Streamlit

## Project Structure

```
Diabetes-Prediction-Model/
├── Diabetes_Prediction.ipynb   # Notebook: data exploration, training, and model export
├── app.py                      # Streamlit web app for making predictions
├── diabetes.csv                # Dataset used for training
├── diabetes_model.pkl          # Trained model (saved with joblib)
└── README.md
```

## Dataset

The model is trained on the **Pima Indians Diabetes Dataset**, which includes the following features:

| Feature | Description |
|---|---|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skinfold thickness (mm) |
| Insulin | 2-hour serum insulin (mu U/ml) |
| BMI | Body mass index |
| Diabetes Pedigree Function | Likelihood of diabetes based on family history |
| Age | Age in years |

The target variable indicates whether the patient has diabetes (1) or not (0).
