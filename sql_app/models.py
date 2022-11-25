from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from db import Base

class Center(Base):
    __tablename__ = 'centers'

    center_id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    city_code = Column(Integer, nullable=False)
    region_code = Column(Integer, nullable=False)
    op_area = Column(Float, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False)
    center_id = Column(Integer, ForeignKey('centers.id'))
    meal_id = Column(Integer, nullable=False)
    checkout_price = Column(Float, nullable=False)
    base_price = Column(Float, nullable=False)
    email_for_promotion = Column(Boolean, nullable=False)
    homepage_featured = Column(Boolean, nullable=False)
    num_orders = Column(Integer, nullable=False)


