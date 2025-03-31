from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import TransactionIn
from rules import check_duplicates, check_currency, check_timestamp_order
from db import SessionLocal
from db_models import Transaction

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/validate")
def validate(transactions: list[TransactionIn]):
    duplicates = check_duplicates(transactions)
    invalid_currency = check_currency(transactions, ["USD", "INR", "EUR"])
    ordered = check_timestamp_order(transactions)
    
    return {
        "duplicates": duplicates,
        "invalid_currencies": invalid_currency,
        "timestamps_in_order": ordered
    }
