# drug_prediction_project
This project predicts the most suitable drug for a patient based on medical attributes using machine learning. The model is trained on the Drug200 dataset and deployed through a Flask web interface.

# 🔍 Project Overview

This ML model predicts the correct drug type by analyzing patient details such as age, sex, blood pressure, cholesterol level, and sodium-to-potassium ratio. The project combines machine learning with a simple web interface for real-time prediction.


# 🧠 Machine Learning Algorithm Used

Random Forest Classifier

Ensemble algorithm made of multiple decision trees

High accuracy and stable predictions

Works well for classification tasks

Handles noisy or categorical data easily

# 📁 Dataset Used

Drug200.csv

Attribute	Description

Age	Patient age
Sex	Male/Female
BP	Blood Pressure (High / Normal / Low)
Cholesterol	High / Normal
Na_to_K	Sodium-to-Potassium ratio
Drug	Output label (Drug A, B, C, X, Y)

# 🛠 Tech Stack

Python

Pandas, NumPy

Scikit-learn

Flask

HTML, CSS


# 🧪 Model Training Steps

1. Load dataset
2. Encode categorical values
3. Split dataset into training/testing
4. Train RandomForestClassifier
5. Evaluate accuracy
6. Save model as model.pkl

# 🌐 Web Interface

The Flask interface allows user input for:
Age
Sex
BP
Cholesterol
Na_to_K

On clicking Predict → shows:
"Predicted Drug: DrugX"

# 📂 Project Structure

Drug-Prediction-Project/
│
├── app.py
├── model.pkl
├── drug200.csv
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

# ▶ How to Run

1. Install dependencies
pip install -r requirements.txt

2. Run Flask app
python app.py

3. Open browser
http://127.0.0.1:5000/

# 📌 Features

Simple and clean UI

Fast predictions

Accurate Random Forest model

Easy to run on any system

Beginner-friendly ML + Flask project

# 👩‍💻 Author

Khushi Pande
