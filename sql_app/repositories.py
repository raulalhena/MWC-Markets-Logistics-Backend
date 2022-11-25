from sqlalchemy.orm import Session
from . import models

class CenterRepository:

 def fetch_by_id(db: Session,_id):
     return db.query(models.Center).filter(models.Center.id == _id).first()
 
 
 def fetch_all(db: Session, skip: int = 0, limit: int = 10):
     return db.query(models.Center).all()
 