#Magic 8 ball
# watch https://youtu.be/WSaS17CSS4c?si=yTQ6Wz-Px6rTh5_u

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
       return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
question=  input('What is your Yes or No question? ')
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
