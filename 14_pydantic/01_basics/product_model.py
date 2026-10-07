from pydantic import BaseModel
# Things to remember 
# Always use type Annotation
# set sensible default
# pydantic convert automaticaly
# "123" --> 123
# 123 --> 123.00


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product1 = Product(id=1, name="candy", price=22, in_stock=True)
product2 = Product(id=2, name="mouse", price=22.22)
product3 = Product(id=2) # give error