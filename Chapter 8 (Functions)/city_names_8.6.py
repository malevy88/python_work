# write a function called city_country() that takes in a name of a city and
# its country. The function should return a string formatted like this:
# Santiago, Chile
# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return (city.title() + ", " + country.title())


city = city_country('santiago', 'chile')
print(city)
city = city_country('paris', 'france')
print(city)
city = city_country('tokyo', 'japan')
print(city)
