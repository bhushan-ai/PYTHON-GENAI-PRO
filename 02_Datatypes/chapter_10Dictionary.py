# Create dictionary
chai_order = dict(type = "Masala tea", size = "Medium", sugar = 2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe['base']}")
print(f"chai recipe: {chai_recipe}")

# delete
del chai_recipe["liquid"]
print(f"chai recipe: {chai_recipe}")

print(f"is sugar in order: {"sugar" in chai_order}")

chai_order = {"type" : "ginger tea" , "size" : "Medium", "sugar": 1}

# methods

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (Items): {chai_order.items()}")


# popitem()
last_item = chai_order.popitem()
print(f"remove last item: {last_item}")

# update()
extra_spices = {"cardamom" : "crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

# safe way to get the values 
customer_note = chai_order.get("note","No note")
print(f"Customer note is: {customer_note}")

