import random
secret = random.randint(1,101)
counter = 0
while True:
    guess = int(input('What is your guess? '))
    counter += 1
    if guess == -1:
        print(f'You could have solved it.  You gave up after {counter} attempts.')
        break
    if guess == secret:
        print(f'Congratulations.  You solved it in {counter} attempts')
        break
    elif guess < secret:
        print(f'Guess {guess} is too low. Try again.  (-1 to give up)')
    else:
        print(f'Guess {guess} is too high. Try again.  (-1 to give up)')

print('Thanks for playing')
    
