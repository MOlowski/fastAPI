from posixpath import basename
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    product: str
    quantity: int
    price: float
    description: str
    
class ItemUpdate(BaseModel):
    product: str
    quantity: str
    body: str
    price: float

class ItemList(Item):
    id: int

    class Config:
        orm_mode = True

class ItemDetail(Item):
    id: int

    class Config:
        orm_mode = True

class ItemCreate(Item):
    pass