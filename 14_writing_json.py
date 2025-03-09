import json
username, role = input('What is your name and role?: ').split()
filename = 'username.json'
with open(filename, 'w') as file_object:
    user_data = {'username':username, 
                 'role': role}
    json.dump(user_data, file_object)
    print('Thanks')
    