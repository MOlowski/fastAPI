from ast import In
import email
from numbers import Real
from sqlalchemy import Column, DateTime, ForeignKey, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    product_id = Column(Integer, ForeignKey("item.id"))
    product = Column(String, ForeignKey("item.product"))
    
    item = relationship("Item")