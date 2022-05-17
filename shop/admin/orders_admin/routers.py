from urllib import response
from fastapi import Depends, status, HTTPException, APIRouter
from orders import cruds, schema, models
from accounts.authentication import get_current_user_admin
from starlette.responses import JSONResponse
from typing import List


router = APIRouter(
    tags=['Admin Accounts'],
    prefix='/admin/orders',
    dependencies=[Depends(get_current_user_admin)]
)


#admin
#update order
@router.put("/orders/{order_id}")
def update_order(order_id: int, order: schema.Order, ):
    update_order = db.query(models.Order).filter(models.Orderid.id==order_id).first()
    
    if update_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="order with given id doesn't exist")
    update_order.product_id = order.product_id
    update_order.quantity = order.quantity
    update_order.price = order.price

    db.commit()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "order update"}
    )

#admin
#delete order
@router.delete("/orders/{order_id}")
def del_order(order_id: int, user_id: int):
    delete_order = db.query(models.Order).fliter(models.Order.order_id==order_id).delete()
    
    db.commit()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "order delete"}
    )