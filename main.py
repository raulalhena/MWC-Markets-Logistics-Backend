from fastapi import Depends, FastAPI, HTTPException
from sql_app import models
from db import get_db, engine
from sqlalchemy.orm import Session
from sql_app.repositories import CenterRepository
from sql_app.repositories import OrderRepository
from db import get_db, engine
from typing import List,Optional
import json
import uvicorn
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/center")
def get_all_items(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    return CenterRepository.fetch_all(db)


@app.get("/order/{center_id}")
def get_all_items(center_id: int, db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    return OrderRepository.fetch_all(db, center_id)

@app.get("/center/ordersforecast/{center_id}")
def get_all_items(center_id: int):
    with open('predictions.json') as file:
        data = json.load(file)
    centers = []
    for i, center in enumerate(data):
        if center["center_id"] == center_id:
            centers.append(center)
    return centers


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
    )

