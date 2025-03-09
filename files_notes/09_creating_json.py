accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}
import json
with open('accounts2.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)
print('reading the data ====\n')

with open('accounts2.json', 'r') as accounts:
    accounts_json = json.load(accounts)
print(accounts_json)
print(accounts_json['accounts'])
print(accounts_json['accounts'][0])
