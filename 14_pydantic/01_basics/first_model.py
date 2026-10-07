from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# pydantic try to convert into its initialization type
input_data = { 'id' : 101, "name" :"op", 'is_active': True }
# input_data = { 'id' : 101, "name" :"op", 'is_active': 25 } validation error

user = User(**input_data) # unpack/ expand dict using **
print(user)