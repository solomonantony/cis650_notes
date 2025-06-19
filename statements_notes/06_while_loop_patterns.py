#The while true: loop pattern is useful for setting up interactive user interfaces.
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

while True:
    question=  input('Enter your Yes/No type question: ')
    print(messages[random.randint(0, len(messages) - 1)])
    if input('Do you want to try again? Y/N ') in 'Nn':
        break
print('Thanks for playing!')
