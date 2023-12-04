# make a list of five or more usernames called current_users
# make another list of five usernames called new_users. Make sure one or two of
# new usernames are also in the current_users list.
# loop through the new_users list to see if each new username has already been
# used. If it has, print a message that the person will need to enter a new
# username. If a username has not bee used, print a messhae saying the username
# is available. Make sure the your comparison is case insensitive. If 'John'
# has been used, 'JOHN' should not be accepted. (To do this, you'll need to make
# a copy of current_users containing the lowercase versions of all exisiting
# users.)

current_users = ['Michael', 'tommy', 'grant', 'Michelle', 'marcus']
new_users = ['Karen', 'lindsey', 'michael', 'Marcus', 'cole']


# creates a copy of current_users list and makes it lower case (need practice)
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # correct answer below
    if new_user.lower() in current_users_lower:
        # if new_user == current_users: (original answer I put)
        print("Sorry " + new_user + ", that username is already taken")
    else:
        print("Hello " + new_user + ", that username is available!")
