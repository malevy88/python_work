# make several dictionaries, where each dictionary represents a different pet.
# in each dictionary, include the kind of animal and the owner's name.
# store these dictionaries in a list called pets.
# next loop through your list and as you do, print everything you know about
# each pet.

pet_1 = {
    'type': 'cat',
    'name': 'Milo',
    'owner_first_name': 'Lindsey',
    'owner_last_name': 'Levy',
}

pet_2 = {
    'type': 'cat',
    'name': 'Thanos',
    'owner_first_name': 'Marcus',
    'owner_last_name': 'Levy',
}

pet_3 = {
    'type': 'turtle',
    'name': 'Steve',
    'owner_first_name': 'Marcus',
    'owner_last_name': 'Levy',
}

pet_4 = {
    'type': 'bird',
    'name': 'Tyson',
    'owner_first_name': 'Angus',
    'owner_last_name': 'Barsch',
}

pet_5 = {
    'type': 'dog',
    'name': 'Brodie',
    'owner_first_name': 'Deandre',
    'owner_last_name': 'Wilson',
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    type = pet['type']
    name = pet['name']
    full_name = pet['owner_first_name'] + ' ' + pet['owner_last_name']
    print(f"This is {name}! The owner is {full_name} and it is a {type}!")
