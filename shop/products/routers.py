from fastapi import APIRouter, Depends, FastAPI, status, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from database import SessionLocal
from . import schema
from . import cruds
from . import models
from typing import List

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


#get all items
#all
@router.get("/items", response_model=List[schema.ItemList], status_code=status.HTTP_200_OK)
def get_all_items():
    return paginate(db.query(Item))

#user
#get item details
@router.get("/items/{item_id}", response_model=schema.ItemDetail, status_code=status.HTTP_200_OK)
async def get_item_details(item_id: int):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    
    if item is None:
        raise HTTPException(status_code=400, detail= "Item with given id doesn't exist")

    return item


