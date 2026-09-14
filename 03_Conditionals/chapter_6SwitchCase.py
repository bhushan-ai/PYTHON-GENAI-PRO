seat_type = input("Enter seat type (sleeper/Ac/luxury/general): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air condition, comfy ride")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case "general":
        print("General - cheapest option")
    case _:
        print("Invalid seat type")