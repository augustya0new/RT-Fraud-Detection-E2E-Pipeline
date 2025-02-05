from fastapi import FastAPI
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("fraud_model.pkl", "rb"))

app = FastAPI()

@app.post("/predict")
def predict(transaction: dict):
    df = pd.DataFrame([transaction])
    prediction = model.predict(df)
    return {"fraud": bool(prediction[0])}
