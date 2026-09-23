class Chai:
    tempereture = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.tempereture)

cutting.tempereture = "Mild"
cutting.cup = "small"
print("After changing: ", cutting.tempereture)
print("cup size is: ", cutting.cup)
print("Direct look into the class: ", Chai.tempereture)

del cutting.tempereture
del cutting.cup
print(cutting.tempereture)
# print(cutting.cup)
