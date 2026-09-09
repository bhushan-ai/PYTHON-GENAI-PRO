# Set declares using {}
essential_spices = {"cardamom", "ginger" , "Cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# Union
all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

# Intersection
common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only Essential Spices: {only_in_essential}")

print(f"Is 'Cloves' in optional Spices? {"cloves" in optional_spices}")
