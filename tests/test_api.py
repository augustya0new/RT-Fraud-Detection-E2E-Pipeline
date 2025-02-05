from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"transaction_amount": 5000, "account_balance": 2000, "device_type_Mobile": 1})
    assert response.status_code == 200
    assert "fraud" in response.json()