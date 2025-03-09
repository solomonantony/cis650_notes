import json
with open("patients.json", 'r') as example:
    example_json = json.load(example)
print('just the keys ===', example_json.keys())
patients_data = example_json['patients']
print(len(patients_data), ' patients')
for patient in patients_data:
    print(patient)
    