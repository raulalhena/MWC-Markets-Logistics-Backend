from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base

class Center(Base):
    __tablename__ = 'centers'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'))
    num_orders = Column(Integer, nullable=False)

