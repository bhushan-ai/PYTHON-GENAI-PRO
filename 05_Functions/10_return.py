# def make_chai():
#     return "Here is your masala chai"

# returned_value = make_chai()
# print(returned_value)
# print(make_chai())

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if  cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(1))


def chai_report():
    return 100, 20, 10 #sold, remaining, left

# if three returns but u want to use 2 
# sold, remaining, _ = chai_report()
sold, remaining, left = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
print("Left: ", left)