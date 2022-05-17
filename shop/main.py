import uvicorn
import os
from fastapi import Depends, FastAPI, status, HTTPException
from database import SessionLocal
from pydantic import BaseModel
from decouple import config

from accounts.models import User
from accounts.routers import router as users_routers

from admin.products_admin.routers import router as admin_products_routers
from admin.accounts_admin.routers import router as admin_accounts_routers
from admin.orders_admin.routers import router as admin_orders_routers

from carts.models import Bin
from carts.routers import router as carts_routers

from orders.models import Order, Orderid
from orders.routers import router as orders_routers

from products.models import Item
from products.routers import router as products_routers


app = FastAPI()

db = SessionLocal()


@app.get("/")
async def root():
    return {"message":"Hello World"}


app.include_router(carts_routers)
app.include_router(users_routers)
app.include_router(products_routers)
app.include_router(orders_routers)
app.include_router(admin_products_routers)
app.include_router(admin_accounts_routers)
app.include_router(admin_orders_routers)







#1
#zmiana formatu usera i przesłąnie do wyświetlenia
#check(do sprawdzenia)
#2
#paginacja
#check(do sprawdzenia)
#3
#aktualizacja itemów i userów
#check
#4
#dodawanie itemów do koszyka
#check
#5
#dodawanie zamówień, edytowanie i usuwanie
#check
#6
#dodanie uprawnień admina, hashowanie hasła
#check
#7
#rozmieszczenie po folderach projektu
#check
#8
#dodanie zdjec do produktow
#??
