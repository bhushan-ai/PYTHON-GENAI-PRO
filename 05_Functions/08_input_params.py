# chai =  "Ginger Tea"

# def prepare_chai(chai):
#     print("Preparing: ", chai)

# prepare_chai(chai)
# print(chai)


chai = [1, 2, 3] #mutable list

def edit_chai(cup):
    cup[1] = 23

edit_chai(chai)
print(chai)


# args
# kwargs

#args
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Dargeeling","Yes", "low")
make_chai(tea="Green", sugar="medium", milk="No")

#kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)


special_chai("Cinnamon", "Cardamom", sweatener="Honey", foam="Yes")
#ingredients gets the tuple all we have
#extras gets the dictionaries


# default args
# def chai_order(order= []):
#     order.append("Masala")
#     print(order)

# chai_order()

def chai_order(order=None):
    if order is None:
        order= []
    print(order)

chai_order()