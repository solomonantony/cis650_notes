# Functions with Multiple Arguments
def maximum(value1, value2, value3):  #defintion of function named maximum with three parameters
    """Return the maximum of three values."""
    max_value = value1  #store value1 to max_value
    if value2 > max_value: # if value2 is greater than max_value
        max_value = value2 # store value2 to max_value
    if value3 > max_value: # if value3 is greater than max_value
        max_value = value3 # store value3 to max_value
    return max_value  # now that max_value has the highest value, return the value

best_grade = maximum(87, 90, 99)
print(best_grade)
print(value2) # why does this line cause an error? Write your answer below as a comment
