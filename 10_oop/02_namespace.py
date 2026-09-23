class Chai:
    origin = "India"

print(Chai.origin)
Chai.chai_is_hot = True
print(Chai.chai_is_hot)


#creating object
masala = Chai()
print(masala.origin)
print(masala.chai_is_hot)

#update values using object
masala.chai_is_hot =  False
print(masala.chai_is_hot)
masala.flavor = "masala"
print(masala.flavor)