flavours = ["masala", "Out of stock", "lemon", "Discontinued", "ginger"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")


print("Out side of the loop")