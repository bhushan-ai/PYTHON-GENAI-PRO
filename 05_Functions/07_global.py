chai_type = "masala"

def update_order():
   def kitchen():
      global chai_type #use to access global varible in function
    #   print("global chai ", chai_type)
      chai_type = "Lemon"
   kitchen()
 

update_order()
print("Final global chai ", chai_type)