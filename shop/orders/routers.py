from fastapi import Depends, status, APIRouter
from starlette.responses import JSONResponse
from accounts.authentication import get_current_user
from .models import Order, Orderid
from products.models import Item
from accounts.schema import User
from carts.models import Bin
from . import cruds
from . import schema


router = APIRouter(
    tags=['Orders'],
    prefix='/orders'
)


#user
#add order
#dodac zmiane liczby produktow po zamowieniu
@router.post("/orders", response_model=schema.Order)
def add_order(db_item: schema.Order, user: User = Depends(get_current_user)):
    items_to_order = db.query(Bin).filter(Bin.user_id==user.id).all()
    
    final_price = 0
    
    for item in items_to_order:
        final_price += item.price * item.quantity
        db_item = models.Order(
            product_id = item.product_id,
            quantity = item.quantity,
            price = item.price
        )

        #check if quantity is possible
        cruds.check_quantity(item.product_id, item.quantity)

        db.add(db_item)

        #delete items from user cart
        db_product_to_del = db.query(Bin).filter(Bin.product_id==item.product_id and Bin.user_id==user.id).first()
        db.delete(db_product_to_del)
        
        #update item quantity
        cruds.change_quantity(item.product_id, item.quantity)

    new_order = Orderid(
        total_price = final_price
    )

    db.add(new_order)
    db.commit()

    return new_order


