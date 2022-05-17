from numbers import Real
from re import L
import string
from typing import List
from sqlalchemy import Column, DateTime, ForeignKey, Text, Float, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base



class Bin(Base):
    __tablename__ = "bin"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer,ForeignKey("item.id"))
    user_id = Column(Integer,ForeignKey("user.id"))
    quantity = Column(Integer)

    item = relationship("Item", back_populates="bin")
    user = relationship("User", back_populates="bin")
