months = {'January': 1, 'February': 2, 'March': 3}
print ('keys', list(months.keys()))
print ('values ', list(months.values()))
print ('items', list(months.items()))
for month_name in sorted(months.keys()):  # to process in sorted order
     print(month_name, end='  ')