from email.mime import image
from fileinput import filename
from math import prod
from typing import List, Optional
from fastapi import APIRouter ,HTTPException ,Depends, status, File, UploadFile, Form
from accounts.authentication import get_current_user_admin
from pydantic.types import NonNegativeFloat
from starlette.responses import JSONResponse
from werkzeug.utils import secure_filename
from products import schema, cruds, models
import uuid, shutil

router = APIRouter(
    tags=['Admin Accounts'],
    prefix='/admin/products',
    dependencies=[Depends(get_current_user_admin)]
)


#admin
#add item
@router.post("/items", response_model=schema.ItemDetail, status_code=status.HTTP_201_CREATED)
def add_item(item:schema.Item):

    db_item = db.query(models.Item).filter(models.Item.product==item.product).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail= "Item already exists")

    new_item = models.Item(
        product=item.product, 
        quantity=item.quantity, 
        price=item.price,
        image=Form(...)
    )

    db.add(new_item)
    db.commit()
    return new_item


#admin
#delete item
@router.delete("/items/{item_id}")
def del_item(item_id: int):
    item_to_delete = db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item with given id doesn't exist")

    db.delete(item_to_delete)
    db.commit()

    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"message": "User delete"}
    )


#admin
#item update
@router.put("/items/{item_id}", response_model=schema.ItemDetail)
async def item_update(
    item_id: int,
    product: Optional[str] = None,
    quantity: Optional[int] = None,
    price: Optional[float] = None,
    description: Optional[str] = None,
    image: UploadFile = File(None)
    ):
    if image:
        filename = f'media/items/{uuid.uuid1()}_{secure_filename(image.filename)}'
        with open(f'{filename}','wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
    update_item = cruds.get_product(item_id)
    update_item.product = product or update_item.product
    update_item.quantity = quantity or update_item.quantity
    update_item.price = price or update_item.price
    update_item.description = description or update_item.description
    update_item.image = filename or update_item.image

    db.commit()

    return update_item

@router.get("/items/{item_id}", response_model=schema.ItemDetail, status_code=status.HTTP_200_OK)
async def get_item_details(item_id: int):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    
    if item is None:
        raise HTTPException(status_code=400, detail= "Item with given id doesn't exist")

    return item