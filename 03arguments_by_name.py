def full_name(last_name, first_name='Bob'):
    """Concatenates first and last names and returns it"""
    return f'{first_name} {last_name}'

print(full_name('Joe','Cool'))  #arguments assigned by place
print(full_name(last_name='daBoss', first_name='Joe')) #arguments assigned by name
print(last_name) # why does this line cause an error? Write your answer below as a comment
