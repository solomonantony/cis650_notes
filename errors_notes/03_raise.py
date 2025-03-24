while True:
    try:
        input_value = float(input('Enter a positve number: '))
        if input_value < 0:
            raise
        reciprocal = 1 / input_value
        break
    except:
        print("Error")


print(f'The reciprocal of {input_value} is {reciprocal:.3f}')




        