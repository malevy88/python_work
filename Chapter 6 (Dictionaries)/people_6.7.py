# start with the program you wrote for 6.1.
# make two new dictionaries representing different people, and store all three
# dictionaries in a list called people.
# loop through your list of people.
# as you loop through the list, print everything you know about each person.

friend_0 = {
    'first_name': 'Deandre',
    'last_name': 'Wilson',
    'age': 33,
    'city': 'Milwaukee',
}

friend_1 = {
    'first_name': 'Tim',
    'last_name': 'Callen',
    'age': 31,
    'city': 'Wauwatosa',
}

friend_2 = {
    'first_name': 'Angus',
    'last_name': 'Barsch',
    'age': 31,
    'city': 'Los Angeles',
}

people = [friend_0, friend_1, friend_2]

for friend in people:
    full_name = friend['first_name'] + " " + friend['last_name']
    friend_age = friend['age']
    friend_city = friend['city']
    print(f"My friend, {full_name} is from {friend_city}, and is {friend_age} "
          "years old!")
