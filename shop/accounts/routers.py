
from fastapi import APIRouter, Depends, FastAPI, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
from typing import List
from .authentication import authenticate_user, get_current_user
from .utils import Hash
from . import models
from . import cruds
from . import schema
from database import SessionLocal
from pydantic import BaseModel
import jwt
import settings
from database import SessionLocal

db = SessionLocal()

router = APIRouter(
    tags=['Accounts'], 
    prefix='/accounts'
)


@router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    user = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'age': user.age,
        'is_active': user.is_active,
        'is_admin': user.is_admin
    }
    token = jwt.encode(user, settings.JWT_SECRET)
    return {'access_token': token, 'token_type': 'bearer'}


#user
#get user info
@router.get("/users/me", response_model=schema.User, status_code=status.HTTP_200_OK)
async def get_user(user: schema.User = Depends(get_current_user)):
    return user



#user
#signup user
@router.post("/users/signup", response_model=schema.User)
def sign_user(user: schema.UserCreate):

    db_user = db.query(models.User).filter(models.User.username==user.username).first()

    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "user already exists")

    new_user = models.User(
        username=user.username, 
        email=user.email,
        age=user.age,
    )

    db.add(new_user)
    db.commit()

    return new_user


#user
#user update
@router.put("/users/{user_id}", response_model=schema.UserUpdate, status_code=status.HTTP_200_OK)
def user_update(user_id: int, user: schema.UserUpdate = Depends(get_current_user)):
    update_user = db.query(models.User).filter(models.User.id==user_id).first()
    update_user.email = user.email
    update_user.age = user.age
    if cruds.email_check(user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user with given email already exist"
        )
    db.commit()

    return update_user


#change password
@router.put("users/change_password")
async def change_password(data: schema.ChangePassword, user: schema.User = Depends(get_current_user)):
    if Hash.verify(data.old_password, user.hashed_password):
        user.hashed_password = Hash.bcrypt(data.new_password)
        user.save()
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "User change password"}
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": "Old password is incorect"}
    )