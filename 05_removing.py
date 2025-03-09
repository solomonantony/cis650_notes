#Removing a Key–Value Pair
days_per_month = {'January': 31, 'February': 28, 'March': 31}
for month, days in days_per_month.items():
  print(f'{month} has {days} days')
  
if days_per_month.get('April'):
  del days_per_month['April']
else:
  print('April not in the dictionary')

#Remove an entry and show what it is using pop
days_per_month.pop('January')
print(days_per_month)

if 'January' in days_per_month:
  print(days_per_month['January'])
else:
  print('January not in the dictionary')
