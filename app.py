from flask import Flask, render_template, request 
import joblib 
import numpy as np 

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bp = int(request.form['bp'])
    chol = int(request.form['chol'])
    na_to_k = float(request.form['na_to_k'])

    # Prepare input
    features = np.array([[age, sex, bp, chol, na_to_k]])

    # Predict using the model
    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f"Predicted Drug: {prediction}")

if __name__ == "_main_":
    app.run(debug=True)