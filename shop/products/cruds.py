from math import prod
import shutil
from fastapi import HTTPException, status
from werkzeug.utils import secure_filename
from products import schema
from . import models
import uuid
from database import SessionLocal

db = SessionLocal()


def get_products(skip: int = 0, limit: int = 100):
    return list(db.query(models.Item).select().offset(skip).limit(limit))


def create_product(
        product,
        quantity,
        price,
        description,
        image,
        ):
    db_item = models.Item(
        product = product,
        quantity = quantity,
        price = price,
        description = description,
        image = image
    )
    db.add(db_item)
    db.commit()
    return db_item


def upload_image_product(image, product_id):
    filename = f'media/product_galleries/{uuid.uuid1()}_{secure_filename(image.filename)}'
    with open(f'{filename}', 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)
    db.query(models.Item).filter(product=product_id, image=filename).save()



def delete_product(product_id: int):
    product = db.query(models.Item).filter(models.Item.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with given id doesn't exist"
        )
    db.delete(product)
    db.commit()
    return "Done"


def get_product(product_id: int):
    product = db.query(models.Item).filter(models.Item.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with given id doesn't exist"
        )
    return product