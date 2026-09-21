favourite_chais = [
    "Masala chai", "Green tea",   "Masala chai", "lemon tea", "Green tea", "Elaichi chai"
] 

unique_chai = { chai for chai in favourite_chais }
print(unique_chai)

recipe = {
    "Masala Chai" : ["Ginger", "Cardamom", "Clove"],
    "Elaichi Chai" : ["Cardamom", "Milk" ],
    "Spicy Chai" :["Ginger", "Black pepper", "Clove"]
}

unique_spices = { spice for ingredients in recipe.values() for spice in ingredients }
print(unique_spices)