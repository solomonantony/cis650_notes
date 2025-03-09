#simulate 10 rolls of a 6-face die
import random
for roll in range(10):
    print(random.randrange(1, 7), end=' ') #simulates the roll of a die
    