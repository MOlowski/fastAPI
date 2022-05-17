from pydantic import BaseModel, EmailStr
from typing import List


'''
class User(BaseModel):
    id: int
    password: str
    username: str
    email: str
    age: int

    class Config:
        orm_mode = True
'''

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: int

    class Config:
        orm_config = True


class UsernameSchema(BaseModel):
    username: List[str]


class ChangePassword(BaseModel):
    old_password: str
    new_password: str