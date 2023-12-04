# write a function called describe_city() that accepts the name of a city and
# it's country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# call your function for three different cities, at least one of which is not in
# default country.

def describe_city(city, country='USA'):
    print(f"\n{city} is located in {country}")


describe_city('Milwaukee')
describe_city('New York')
describe_city(city='Paris', country='France')
