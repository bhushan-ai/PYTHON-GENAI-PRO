# Append()
ingredients = ["water", "milk", "black tea"]
ingredients.append('sugar')
print(f"Tea Ingredients: {ingredients}")

# remove()
ingredients.remove("water")
print(f"Tea Ingredients: {ingredients}")

# extend()
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"Tea Ingredients: {chai_ingredients}")

# insert : using index number
chai_ingredients.insert(2,"black tea")
print(f"Tea Ingredients: {chai_ingredients}")

# pop() : value on last index remove
last_added = chai_ingredients.pop()
print(f"Chai: {last_added}")
print(f"Tea Ingredients: {chai_ingredients}")

#reverse() the list
chai_ingredients.reverse()
print(f"Tea Ingredients: {chai_ingredients}")

# sort()
chai_ingredients.sort()
print(f"Tea Ingredients: {chai_ingredients}")

# min() max()
sugar_levels = [1, 2, 3, 4, 5]
print(f"Max Sugar levels: {max(sugar_levels)}")
print(f"Min Sugar levels: {min(sugar_levels)}")

# Operator Overloading
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"]  * 3
print(f"Strong Brew: {strong_brew}")

# bytearray
raw_spice_data = bytearray(b"CINNAMON") 
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")