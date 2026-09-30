class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala" : 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be integer")
        total  = menu[flavor] * cups
        print(f"Your bill for {cups} of cup {flavor} chai is {total} rupees")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting our shop")

bill("mint", 2)
bill("masala", "two")
bill("ginger", 3)