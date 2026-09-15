# Zip() iterate over sevral iterable in parallel, producing tuple with an item from each one

names = ["Bhushan", "carlos", "nia", "peter"]
bills =  [20, 30, 100, 40]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")