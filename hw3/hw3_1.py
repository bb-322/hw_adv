import json

dict1 = {}
for i in range(10):
    dict1[f'key{i}'] = f'value{i}'

with open('dict1.json', 'w') as f:
    json.dump(dict1, f, indent=4)


with open('dict1.json', 'r') as f:
    loaded_dict = json.load(f)

for key,value in loaded_dict.items():
    print(f'{key}:', value)