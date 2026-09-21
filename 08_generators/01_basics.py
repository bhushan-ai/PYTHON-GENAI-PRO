# comes with yeild
# u save memory 
# u dont want result immidietely
# lazy evaluation

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for chai in stall:
    print(chai)


def gen_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


print(gen_chai_list())

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) error