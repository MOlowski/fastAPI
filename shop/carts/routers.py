from accounts.authentication import get_current_user
from starlette.responses import JSONResponse
from fastapi import APIRouter ,Depends, status, HTTPException
from . import schema
from . import models
from decimal import Decimal
from products.cruds import get_product
from accounts.schema import User
from accounts.models import User


router = APIRouter(
    tags=['Carts'],
    prefix='/carts'
)


#user
#add item to cart
@router.post("/users/{user_id}/bin")
def add_item_to_bin(user_id: int, item: schema.Bin, user: User = Depends(get_current_user)):

    db_user = db.query(User).filter(User.id==user_id).first()

    if db_user is None:
        raise HTTPException(status_code=400, detail= "User doesn't exist")

    db_item = db.query(models.Bin).filter(models.Bin.product_id==item.product_id).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail= "Item is already added to shopping cart")

    new_item = models.Bin(
        product_id = item.product_id,
        user_id = item.user_id,
        quantity = item.quantity
    )

    db.add(new_item)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "add to cart"}
    )


@router.get("users/{user_id}/bin", response_model=schema.Bin)
async def items_bin(user_id: int, user: User = Depends(get_current_user)):
    items = db.query(models.Bin).filter(models.Bin.user_id == user_id).all()
    return items


#user
#update quantity of item in cart
@router.put("/users/{user_id}/bin", response_model=schema.BinUpdate)
def change_item_quantity_in_cart(user_id: int, bin: schema.BinUpdate, product_id: int, user: User = Depends(get_current_user)):
    update_bin = db.query(models.Bin).filter(models.Bin.user_id==user_id and models.Bin.product_id==product_id).first()
    update_bin.quantity = bin.quantity

    db.commit()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "change quantity of item"}
    )

#user
#delete item from cart
@router.delete("/users/{user_id}/bin")
def delete_item_from_cart(user_id: int, product_id: int):
    delete_item = db.query(models.Bin).fliter(models.Bin.user_id==user_id and models.Bin.product_id==product_id).delete()

    db.commit()

    return delete_item
