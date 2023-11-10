person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

print(person['age'])

for key, value in person.items():
    print(f"\nkey : {key}")
    print(f"value : {value}")