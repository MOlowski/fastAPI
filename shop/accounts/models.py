from email.policy import default
from numbers import Real
from re import L
import string
from typing import List
from sqlalchemy import Column, DateTime, ForeignKey, Text, Float, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    hashed_password = Column(String(255), nullable=False)
    username = Column(String(10), nullable=False, unique=True)
    email = Column(String, unique= True)
    age = Column(Integer)
    is_active = Column(Boolean, default = False)
    is_admin = Column(Boolean, default= False)

    bin = relationship("Bin", back_populates="user")