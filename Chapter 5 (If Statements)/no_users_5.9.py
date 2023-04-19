# Add an if test to hello_admin.py to make sure the list of user is no empty.
# If the list is empty, print the message "We need to find some users!"
# Remove all of the usernames from your list, and make sure the correct message
# printed.

user_names = []

if user_names:
    for user_name in user_names:
        print(f"Hello {user_name}, thanks for logging in")
    else:
        print("We need to fid some users!")
