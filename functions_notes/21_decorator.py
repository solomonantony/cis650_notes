# A decorator is a function that takes another function, adds some behavior around it, and gives back the improved version.
def wave(some_function):
    def wrapper(name):
        print(chr(0x270B))
        some_function(name)
    return wrapper

@wave
def greet(name):
    print(f"hello, {name}")
greet('sam')

