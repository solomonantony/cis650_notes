def full_name(last_name, first_name='Bob'):
    """Concatenates first and last names and returns it"""
    return f'{first_name} {last_name}'

print(full_name('Cool'))  #arguments assigned by place
print(full_name(first_name='Joe', last_name='daBoss')) #arguments assigned by name
print(last_name) # why does this line cause an error? Write your answer below as a comment
