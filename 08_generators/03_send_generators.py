def chai_customer():
    print("Welcome! What chai would u like?")
    order = yield
    while True:
        print(f"preparing: {order} chai")
        order = yield

stall = chai_customer()
next(stall)
chai = input(": ")
stall.send(chai)