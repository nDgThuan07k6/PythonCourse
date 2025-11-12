import json

json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'

data = json.loads(json_str)
print('Name:', data['name'])
print('Age:', data['age'])
print('City:', data['city'])

json_result = json.dumps(data)
print('Json type after:', json_result)