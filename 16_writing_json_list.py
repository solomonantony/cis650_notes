import json
with open("patients.json", 'w') as example:
    example_json = json.load(example)
print('just the keys ===', example_json.keys())
patients_data = example_json['patients']
print(len(patients_data), ' patients')
#get patient information
new_patient = {}
for key in patients_data[0].keys():
    new_patient[key] = input(f'Enter {key}: ')
print(new_patient)

    