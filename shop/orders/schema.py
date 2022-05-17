from posixpath import basename
from pydantic import BaseModel



class Order(BaseModel):
    id: int
    quantity: int
    price: float
    
    class Config:
        orm_mode = True

class Orderid(BaseModel):
    id: int
    price: float

    class Config:
        orm_mode = True
        
