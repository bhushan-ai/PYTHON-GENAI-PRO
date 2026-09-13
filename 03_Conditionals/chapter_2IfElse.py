snack = input("Enter your prefered Snack: ").lower()

print(f"User said: {snack}")

if snack == "samosa" or snack == "cookies":
    print(f"Great Choice!, We'll  serve you {snack}")
else:
    print("Sorry, we only serve cookies and samosa")
