from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the pre-trained model and TF-IDF vectorizer
model = joblib.load('models/model.joblib')
tfidf = joblib.load('models/tfidf.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email = request.form['email']
        
        # Transform the email text using the TF-IDF vectorizer
        email_vectorized = tfidf.transform([email])
        
        # Predict using the loaded model
        prediction = model.predict(email_vectorized)
        
        # Return the result
        if prediction == 1:
            result = "This is a spam email."
        else:
            result = "This is not a spam email."
        
        # Pass both the email content and result to the template
        return render_template('index.html', result=result, email=email)

if __name__ == '__main__':
    app.run(debug=True)
