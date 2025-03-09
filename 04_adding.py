days_per_month = {'January': 31, 'February': 28, 'March': 31}
for month, days in days_per_month.items():
    print(f'{month} has {days} days')

#Accessing the Value Associated with a Key;  Use square brackets
days_per_month['January']

#Updating the Value of an Existing Key–Value Pair
days_per_month['February'] = 29

#Adding a New Key–Value Pair
days_per_month['April'] = 30
days_per_month

#check if a key exixsts before accessing it
if not days_per_month.get('May'):
  print('May not found')
