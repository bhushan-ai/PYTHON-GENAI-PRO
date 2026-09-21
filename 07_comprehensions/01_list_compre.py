menu = [
    "Masala Tea",
    "Iced Lemon tea",
    "Green tea",
    "Iced peach tea",
    "Ginger tea" 
]

# iced_tea = [tea for tea in menu if "Iced" in tea]
# iced_tea = [tea for tea in menu if len(tea) < 10]
iced_tea = [tea for tea in menu if len(tea) > 10]

print(iced_tea)