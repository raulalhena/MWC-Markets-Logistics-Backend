from dotenv import load_dotenv
load_dotenv()

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:NkxlMh9DS8@postgres.cgguaffp7qy0.us-east-1.rds.amazonaws.com:5432/postgres'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={},echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()