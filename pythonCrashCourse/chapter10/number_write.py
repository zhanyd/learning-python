import json

numbers = [2,3,3,2,6,77,21]

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename, 'r') as f:
    numbers = json.load(f)
    print(numbers)