from . import models, schema
from .utils import Hash
from database import SessionLocal

db = SessionLocal()


def get_user(user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(db.query(models.User).select().offset(skip).limit(limit))

def create_user(user: schema.UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(
        email = user.email,
        hashed_password = hashed_password,
        is_active = False,
        is_admin = False
    )
    db.add(db_user)
    db.commit()
    return db_user
    
def email_check(user:schema.User):
    db_check = db.query(models.User).filter(models.User.email==user.mail).first()
    if db_check is not None:
        return False
    return True