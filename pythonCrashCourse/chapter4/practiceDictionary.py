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

pets = [
    {
        "type" : "dog",
        "name" : "Max",
        "age" : 2
    },
    {
        "type" : "cat",
        "name" : "Kitty",
        "age" : 5
    },
    {
        "type" : "fish",
        "name" : "Sushi",
        "age" : ""
    }
]    

for pet in pets:
    '''注释'''
    for key, value in pet.items():
        print(f"\nkey : {key}")
        print(f"value : {value}")

def describe_pet(pet_name, pet_type = "dog"):
    """Display information about a pet."""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name}.")

describe_pet("ww")
