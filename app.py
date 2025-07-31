from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models and vectorizer
vectorizer = joblib.load("Models/vectorizer.pkl")
models = {
    "BernoulliNB": joblib.load("Models/MRSA_bnb.pkl"),
    "MultinomialNB": joblib.load("Models/MRSA_mnb.pkl"),
    "GaussianNB": joblib.load("Models/MRSA_gnb.pkl")
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        model_name = request.form['model']
        model = models.get(model_name)
        
        if model:
            transformed = vectorizer.transform([review]).toarray()
            prediction = model.predict(transformed)[0]
            sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
            return render_template('index.html', prediction=sentiment, review=review, selected_model=model_name)
        else:
            return "Model not found"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
