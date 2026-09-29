chai_menu = {"masala" : 30, "ginger": 40}

try: 
    chai_menu["elaichi"]
except KeyError:
    print("The key that u r typing to access is not exist")