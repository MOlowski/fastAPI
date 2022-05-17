from decouple import config


JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")
EXPIRED_TIME = 900 #15 minutes

