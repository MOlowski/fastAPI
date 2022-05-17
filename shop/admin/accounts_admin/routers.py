from urllib import response
from fastapi import Depends, status, APIRouter
from accounts import cruds, schema, models
from accounts.authentication import get_current_user_admin
from starlette.responses import JSONResponse
from typing import List


router = APIRouter(
    tags=['Admin Accounts'],
    prefix='/admin/accounts',
    dependencies=[Depends(get_current_user_admin)]
)


@router.get("users/", response_model=List[schema.User])
async def get_users(skip: int = 0, limit: int = 100):
    users = cruds.get_users(skip = skip, limit = limit)
    return users

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user:
        db.delete(user)
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"message": "User delete"}
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "User not found"}
    )
    