from posixpath import basename
from pydantic import BaseModel


class Bin(BaseModel):
    id: int
    quantity: int
 
class BinUpdate(BaseModel):
    quantity: int