from database import Base, engine

from accounts.models import User
from products.models import Item
from orders.models import Order, Orderid
from carts.models import Bin


Base.metadata.create_all(engine)