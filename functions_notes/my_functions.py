def get_int(prompt):
    while True:
        try:
            input_value = int(input(prompt))
            return input_value
        except:
            print("Error")

def get_float(prompt):
    while True:
        try:
            input_value = float(input(prompt))
            return input_value
        except:
            print("Error")
