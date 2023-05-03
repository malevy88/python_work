# use the code in favorite_laguages.py
# make a list of people who should take the favorite languages poll.
# include some names that are already in the dictionary and some that aren't.
# loop through the list of people who should take the poll. if they have already
# taken the poll, print a message thanking them for responding. If they have not
# yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

polling_list = (
    'jen', 'phil', 'marcus', 'lindsey', 'edward',
)

for name in polling_list:
    if name in favorite_languages:
        print(f"Thank you {name}, you've completed the poll!")
    else:
        print(f"{name}, please don't forget to take our poll.")
