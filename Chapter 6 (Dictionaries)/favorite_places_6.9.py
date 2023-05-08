# make a dictionary called favorite_places.
# think of three names to use as keys in the dicitonary, and store one to three
# favorite places for each person. to make this exercise a bit more interesting,
# ask some friends to name a few of their favorite places. lopp through the
# dictionary, and print each person's name and their favorite places.

favorite_places = {
    'Marcus': 'New York, NY',
    'Lindsey': 'Milwaukee, WI',
    'Angus': 'Milwaukee, WI',
    'Deandre': 'Houston, TX',
    'Tim': 'Miami, Florida',
}

for name, location in favorite_places.items():
    print(f"{name.title()}'s favorite place to travel is {location}.")
