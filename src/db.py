from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection
DATABASE_URL = "postgresql://user:password@localhost:5432/fraud_db"
engine = create_engine(DATABASE_URL)

def store_fraudulent_transaction(transaction):
    df = pd.DataFrame([transaction])
    df.to_sql("fraudulent_transactions", engine, if_exists="append", index=False)
