import os


from passlib.context import CryptContext


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(plain_password, hashed_password):
        return pwd_cxt.verify(plain_password, hashed_password)
