# dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# for loop to loop through everyone's favorite languages
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionary's keys in a particular order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
# sorted method sorts names by alphabetical order in print
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
