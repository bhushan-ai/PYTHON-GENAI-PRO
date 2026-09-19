# types of function
# pure & impure functions
# recursive function
# lambdas (Anonemous function)

#1. pure function
def pure_chai(cups):
    return cups * 10

total_chai = 10
# impure functions not recomended
def impure_chai(cups):
    global total_chai
    total_chai += cups


#2. Recursive function
def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))


#3. lambda functions
chai_types = ["light", "kadak", "ginger",  "kadak"]

kadak_chai = list(filter(lambda  chai: chai!= "kadak", chai_types))

print(kadak_chai)