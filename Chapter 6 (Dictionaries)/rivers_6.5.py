# Make a dictionary containing three major rivers and the country each river
# runs through. One key-value pair might be 'nile': 'egypt'
# Use a loop to print a sentence about each river, such as The Nile runs through
# Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

major_rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'indus': 'asia'
}

for river, country in major_rivers.items():
    print(f"\nThe {river} is located in {country}!")

print("\nThese are the rivers mentioned in the previous post")
for river in major_rivers.values():
    print(f"{river}")

print("\nThese are the countries mentioned")
for country in major_rivers.values():
    print(f"{country}")
