contacts = {
    'jsmith@mymail.com': '801-555-1223',
    'jdoe12@mymail.com': '801-555-9887'
}

def add(contacts):
    id = input('email of contact to add/update: ')
    phone = input('phone of contact to add/update: ')
    contacts[id] = phone

def delete(contacts):
    key = input('email of contact to delete: ')
    if key in contacts: del contacts[key]
    else: print('Error, email not found in contacts')

def display(contacts):
    for email, phone in contacts.items():
        print(email, phone, sep='\t')

def menu():
    print('+ add  - delete  * display  / quit  ? help')

menu()
command = input('action: ')
while command not in  ('', '/'):
    if   command == '+': add(contacts)
    elif command == '-': delete(contacts)
    elif command == '*': display(contacts)
    elif command == '?': menu()
    else: print('Unknown command')
    command = input('action: ')
    