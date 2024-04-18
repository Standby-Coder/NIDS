from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load ML models
models = {
    'gaussian_naive_bayes': joblib.load('./models/model1.pkl'),
    'decision_tree': joblib.load('./models/model2.pkl'),
    'random_forest': joblib.load('./models/model3.pkl'),
    'svm': joblib.load('./models/model4.pkl'),
    'logistic_regression': joblib.load('./models/model5.pkl'),
    'gradboost': joblib.load('./models/model6.pkl')
}

def predict_model(model_key, df):
    model = models[model_key]
    return model.predict(df)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from form or file
        if 'file' in request.files and request.files['file'].filename != '':
            df = pd.read_csv(request.files['file'])
        else:
            # Manually entered data
            data = [request.form.get(field, type=float) for field in request.form if field != 'model']
            df = pd.DataFrame([data], columns=[field for field in request.form if field != 'model'])

        # Predict using selected models
        selected_models = request.form.getlist('model')
        results = {model: predict_model(model, df) for model in selected_models}
        
        # Render the results
        return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
