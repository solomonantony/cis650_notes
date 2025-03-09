contacts = {}

print('Enter phone # and email at > prompt (<return> when done)')

entry = input('> ')

while entry != '':
    phone, email = entry.split()
    contacts[phone] = email
    print(contacts)
    entry = input('> ')

print(contacts)
