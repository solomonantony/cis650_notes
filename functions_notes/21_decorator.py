# wrapping a function that uses a parameter
def wave(some_function):
    def wrapper(name):
        print(chr(0x270B))
        some_function(name)
    return wrapper

@wave
def greet(name):
    print(f"hello, {name}")
greet('sam')

