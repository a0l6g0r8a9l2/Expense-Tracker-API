from fastapi import FastAPI, HTTPException
from typing import List
import re
import json
import ssl
import os
import uvicorn
from pydantic import BaseModel
from datetime import datetime

ENV = os.getenv('ENV') or 'DEV'

app = FastAPI()

if ENV.upper() == 'PROD':
    SSL_CERT_PATH = os.getenv('SSL_CERT_PATH')
    SSL_KEY_PATH = os.getenv('SSL_KEY_PATH')
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(SSL_CERT_PATH, keyfile=SSL_KEY_PATH)


class Transaction(BaseModel):
    text: str
    sentTimestamp: datetime
    receivedTimestamp: datetime
    sim: str


class ParsedTransaction(BaseModel):
    amount: float
    currency: str
    description: str


def parse_transaction_text(text: str) -> ParsedTransaction:
    # Предположим, что текст имеет формат: "Payment: <amount> <currency> <description>"
    pattern = r"Payment: (\d+(?:\.\d+)?) (\w+) (.+)"
    match = re.match(pattern, text)
    if match:
        amount = float(match.group(1))
        currency = match.group(2)
        description = match.group(3)
        return ParsedTransaction(amount=amount, currency=currency, description=description)
    else:
        raise HTTPException(status_code=400, detail="Невозможно распознать формат транзакции")


def save_transaction(transaction: ParsedTransaction):
    with open("transactions.json", "a") as file:
        json.dump(transaction.dict(), file)
        file.write("\n")


@app.post("/transactions/")
async def add_transaction(transaction: Transaction):
    parsed_transaction = parse_transaction_text(transaction.text)
    save_transaction(parsed_transaction)
    return {"message": "Транзакция успешно добавлена"}


@app.get("/transactions/", response_model=List[ParsedTransaction])
async def get_transactions(skip: int = 0, limit: int = 10):
    transactions = []
    with open("transactions.json", "r") as file:
        lines = file.readlines()
        for line in lines:
            transaction_dict = json.loads(line)
            transaction = ParsedTransaction(**transaction_dict)
            transactions.append(transaction)
    return transactions[skip: skip + limit]


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        # ssl_keyfile=SSL_KEY_PATH,
        # ssl_certfile=SSL_CERT_PATH
        )
