# Creating file

# file =  open("order.txt", "w")
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()

# new operator with
with open("orders.txt", "w") as file:
    file.write("ginger tea - 2")