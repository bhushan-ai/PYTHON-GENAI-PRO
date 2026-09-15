# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not Divisiblem, remainder is {remainder}")


value = 13

if (remainder := value % 5):
    print(f"Not Divisiblem, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ").lower()) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"{requested_size} is not available")


flavors = ["Masala", "Mint", "Ginger", "lemon"]

print("Available flavors:", flavors)

while (flovor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flovor} is not available")

print(f"You choose {flovor} chai")