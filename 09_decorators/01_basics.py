# decorator
# r wrapper function which takes ur function excute them or add some more to it probabaly print something or inject more values etc.

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before functions runs")
        func()
        print("After functions runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorator class")  


greet()
print(greet.__name__)