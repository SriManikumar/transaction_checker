from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    transaction_id: str
    account_id: str
    amount: float
    currency: str
    timestamp: datetime
