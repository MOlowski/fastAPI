from genericpath import exists
from operator import ge
from typing import List
from uuid import uuid4, UUID
from models import User, Gender, Role, Change
from typing import List
from fastapi import FastAPI, HTTPException


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("0a0037ad-c9d3-4fbf-8aab-f6fd59ece10c"), 
        first_name='Kamil', 
        last_name='Nowak',
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("38613877-cd90-4dc9-9e5a-3ed06d9cbfd2"), 
        first_name='Marcin', 
        last_name='Nowaczkiewicz',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("38613877-cd90-4dc9-9e5a-3ed06d9cbfd2"), 
        first_name='Katarzyna', 
        last_name='Dorsz',
        gender=Gender.female,
        roles=[Role.student, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}")
async def change_user(user_update: Change, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.gender is not None:   
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


