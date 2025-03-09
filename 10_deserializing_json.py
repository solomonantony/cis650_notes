import json
with open('accounts2.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))