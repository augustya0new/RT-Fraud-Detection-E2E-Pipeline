# 🚀 Real-Time Fraud Detection System

## 📌 **Project Overview**
This project implements a **real-time fraud detection system** using **machine learning** and **streaming technologies**. The system predicts fraudulent transactions using a **Random Forest Classifier**, serves predictions via a **FastAPI REST API**, and integrates with **Apache Kafka** for real-time transaction monitoring. Fraudulent transactions are stored in a **PostgreSQL database** for further analysis.

## 🎯 **Key Features**
- ✅ **Machine Learning Model**: Detects fraud with a trained Random Forest classifier.
- ✅ **FastAPI Deployment**: Real-time prediction API.
- ✅ **Kafka Integration**: Streaming transactions for real-time monitoring.
- ✅ **PostgreSQL Storage**: Stores fraudulent transactions.
- ✅ **Dockerized System**: Ready for deployment with Docker & Docker-Compose.
- ✅ **Unit Tests & CI/CD**: Ensuring high reliability.

---

## 📂 **Project Structure**
```
📂 fraud-detection-system
│── 📜 README.md               <- Project overview, setup guide, API docs
│── 📜 requirements.txt        <- Dependencies for environment setup
│── 📜 .gitignore              <- Ignore unnecessary files (logs, data dumps)
│── 📂 data
│   ├── transactions.csv       <- Raw dataset
│   ├── preprocessed.csv       <- Processed dataset
│   ├── kaggle_url.txt         <- URL to dataset: https://www.kaggle.com/datasets/ealaxi/paysim1
│── 📂 notebooks
│   ├── exploratory_analysis.ipynb  <- EDA, feature selection
│   ├── model_training.ipynb        <- Model training, evaluation
│── 📂 src
│   ├── config.py              <- Configuration settings
│   ├── preprocess.py          <- Data cleaning & feature engineering
│   ├── model.py               <- ML model training and inference
│   ├── streaming.py           <- Kafka consumer logic
│   ├── db.py                  <- Database connection (PostgreSQL)
│   ├── main.py                <- FastAPI API for fraud prediction
│── 📂 docker
│   ├── Dockerfile             <- Docker setup for API deployment
│   ├── docker-compose.yml     <- Container orchestration (API + DB + Kafka)
│── 📂 tests
│   ├── test_api.py            <- Unit tests for API
│   ├── test_model.py          <- Unit tests for ML model
│── 📂 docs
│   ├── API_DOCS.md            <- API documentation with usage examples
│   ├── architecture.png       <- System design diagram
│── 📂 .github
│   ├── workflows
│       ├── ci_cd.yml          <- GitHub Actions for CI/CD
```
---

## 📊 **Dataset**
- 📌 **Source**: [PaySim Fraud Detection Dataset - Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)
- 📌 **Description**: A synthetic dataset that simulates mobile money transactions.
- 📌 **Key Features**:
  - `amount`: Amount of transaction.
  - `type`: (e.g., "CASH_OUT", "TRANSFER").
  - `newbalanceOrig`: User’s balance before & after.
  - `oldbalanceDest`: Recipient's balance before.
  - `newbalanceDest`: Recipient's balance after.
  - `is_fraud`: **Target variable** (1 = Fraud, 0 = Legitimate).

---

## 🏗 **Installation & Setup**
### 🔹 **1. Clone the Repository**
```bash
git clone https://github.com/augustya0new/RT-Fraud-Detection-E2E-Pipeline.git
cd fraud-detection-system
```

### 🔹 **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Run Exploratory Data Analysis (EDA)**
Open **`notebooks/exploratory_analysis.ipynb`** in Jupyter Notebook and execute all cells.
```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

### 🔹 **4. Train the Model**
Execute **`notebooks/model_training.ipynb`** to train the fraud detection model.
```bash
jupyter notebook notebooks/model_training.ipynb
```

---

## 🚀 **Running the API Locally**
1️⃣ **Start FastAPI**
```bash
uvicorn src.main:app --reload
```

2️⃣ **Test API (Using cURL)**
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \
-d '{"transaction_amount": 5000, "account_balance": 2000, "device_type_Mobile": 1}'
```

---

## 📡 **Kafka Streaming Integration**
**Start Kafka (Dockerized Setup)**
```bash
docker run -d --name kafka -p 9092:9092 wurstmeister/kafka
```
**Run Consumer**
```bash
python src/streaming.py
```

---

## 🛠 **Docker Deployment**
1️⃣ **Build & Start Containers**
```bash
docker-compose up --build
```
2️⃣ **Access API**
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \
-d '{"transaction_amount": 5000, "account_balance": 2000, "device_type_Mobile": 1}'
```

---

## ✅ **Unit Testing & CI/CD**
Run unit tests before deployment.
```bash
pytest tests/
```
**CI/CD Pipeline (GitHub Actions)**
- Defined in `.github/workflows/ci_cd.yml`.
- Runs tests automatically on push.

---

## ✨ **Contributions & Support**
- **Contributions**: Open a PR or issue.
- **License**: MIT License.
- **Contact**: kumaraugustya1@gmail.com | augustya0new

---
🚀 **Enjoy real-time fraud detection at scale!** 🔥

