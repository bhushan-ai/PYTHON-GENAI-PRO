# Creating file

file =  open("order.txt", "w")
try:
    file.write("Masala Chai - 2 cups")
finally:
    file.close()

# new operator with
with open("orders.txt", "w") as file:
    file.write("ginger tea - 2")

# read the file
file = open("orders.txt", "r")
text = file.read()
print(text)

with open("orders.txt", "r") as file:
    text = file.read()
    print(text)

# append the file
file = open("orders.txt", "a")
file.write("Masala tea - 3")
file.close()

with open("orders.txt", "a") as file:
    file.write("Masala tea - 5")
