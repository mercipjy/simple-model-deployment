# Simple Model Deployment

This project demonstrates how to build a simple linear regression model and deploy it using Flask.

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Train the model:

python model.py

3. Run the Flask app:

python app.py

4. Test the API:

curl -X POST -H "Content-Type: application/json" -d '{"features": [1.5]}' 
http://127.0.0.1:5000/predict

## Requirements
- Python 3.x
- Flask
- Scikit-learn
