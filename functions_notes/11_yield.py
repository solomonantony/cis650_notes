def squares(x):
  for i in range(x):
      print('From def ', i)
      yield i ** 2

print(squares(5))
for i in squares(5):
  print(f'i = {i}')
  