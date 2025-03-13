# simulate 600 rolls of a die and compute frequencies
frequencies = [0, 0, 0, 0, 0, 0]
import random
for i in range(6000):
  roll = random.randint(1,6)
  frequencies[roll-1] += 1
print(frequencies)
for i, x in enumerate(frequencies):
  print(f'Face {i+1} came up {x} times')
  