# make a list of people who should take the favorite language poll.
# include some from the already created dictionary and some that aren't.
# loop thorough the list of people who should take the poll. If they have
# already taken the poll, print a message inviting them to take the poll.

favorite_language = {
    'jen': 'c',
    'marcus': 'javascript',
    'tyson': 'c++',
    'lindsey': 'swift',
    'tim': 'ruby',
}

polling_list = [
    'kathy', 'marcus', 'shawn', 'michael', 'lindsey',
]

for name in polling_list:
    if name in favorite_language:
        print(f"Thanks {name.title()}, you've already taken the poll.")
    else:
        print(f"{name.title()}, please don't forget to take the poll.")
