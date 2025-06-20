import random
# watch https://youtu.be/WSaS17CSS4c?si=yTQ6Wz-Px6rTh5_u
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

question=  input('Enter your Yes/No type question: ')
print(messages[random.randint(0, len(messages) - 1)])
