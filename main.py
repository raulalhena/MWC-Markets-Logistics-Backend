from fastapi import Depends, FastAPI, HTTPException
from sql_app import models
from db import get_db, engine
from sqlalchemy.orm import Session
from sql_app.repositories import CenterRepository
from db import get_db, engine
from typing import List,Optional

app = FastAPI()


@app.get("/center")
def get_all_items(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    return CenterRepository.fetch_all(db)