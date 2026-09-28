# A decorator is a function that takes another function, adds some behavior around it, and gives back the improved version.
def wave(some_function):
    def wrapper():
        print(chr(0x270B))
        some_function()
    return wrapper

@wave
def greet():
    print("hello")
greet()




