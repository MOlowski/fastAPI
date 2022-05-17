from enum import unique
import string
from typing import List
from sqlalchemy import Column, DateTime, ForeignKey, Text, Float, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    description = Column(String)
    image = Column(unique= True)

    order = relationship("Order", back_populates="item")
    bin = relationship("Bin", back_populates="item")