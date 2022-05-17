from numbers import Real
from re import L
import string
from typing import List
from sqlalchemy import Column, DateTime, ForeignKey, Text, Float, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    product_id = ForeignKey("item.id")
    quantity = Column(Integer)
    price = Column(Float)
    order_id = ForeignKey("orderid.id")

    orderid = relationship("Orderid")
    item = relationship("Item")
    user = relationship("User")

class Orderid(Base):
    __tablename__ = "orderid"
    id = Column(Integer, primary_key=True)
    total_price = Column(Float)