class OutOfIngredientError(Exception):
    pass


def make_chai(sugar, milk):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientError("Missing milk or sugar value")
    print("Chai is ready")

make_chai(0,1)