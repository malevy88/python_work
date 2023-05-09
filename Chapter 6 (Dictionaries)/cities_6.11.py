# make a dictionary called cities.
# use names of three cities as keys in your dictionary
# create a dictionary of information abour each city and include the country
# that the city is in, its approximate population, and one fact about the city.
# the keys for each city's dictionary should be something like country,
# population, fact. Print the name of each city and all of the informations
# you have stored about it.

cities = {
    'Milwaukee, WI': {
        'Country': 'USA',
        'Population': 569330,
        'Fact': 'Birthplace of Harley Davidson in 1903',
    },

    'Florence, Tuscany': {
        'Country': 'Italy',
        'Population': 382258,
        'Fact': 'Birthplace of the Renaissance',
    },

    'Paris, Île-de-France': {
        'Country': 'France',
        'Population': 2161000,
        'Fact': 'Has 5 Statues of Liberty',
    }
}

for city, city_info in cities.items():
    print(f"\nCity and State: {city}")
    location = city_info['Country']
    population = city_info['Population']
    fact = city_info['Fact']
    print(f"Country: {location}")
    print(f"Population: {population}")
    print(f"Random fact: {fact}")
