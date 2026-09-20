# import recipe.flavours
# print(recipe.flavours.ginger_chai())

# another way
# from recipe.flavours import elaichi_chai, ginger_chai
# print(elaichi_chai())

#another way .. one directory back
from .recipe.flavours import elaichi_chai
print(elaichi_chai())



