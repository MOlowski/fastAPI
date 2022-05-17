from products.models import Item
from starlette.responses import JSONResponse
from fastapi import status
from database import SessionLocal

db = SessionLocal()


def change_quantity(product_id: int, quantity: int):
    product = db.query(Item).filter(Item.id==product_id).first()
    product.quantity = product.quantity - quantity
    return db.commit()


def check_quantity(product_id: int, quantity: int):
    product = db.query(Item).filter(Item.id==product_id).first()
    if product.quantity >= product.quantity:
        return True
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "There is no possible quantity of item to order"}
        )