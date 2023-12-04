# Make a list of five or more usernames, including the name 'admin'.
# Imagine you are writing a code that will peint a greeting to each user after
# they log in to a website. Loop through the list, and print a greeting to each
# user. If the username is 'admin', print a special greeting, such as Hello
# admin, you like a status report? Otherwise, print a generic greeting, such as
# Hello Jaden, thank you for loggin in again

user_names = ['malevy', 'admin', 'gen34x4', 'local', 'levyma88']

for user_name in user_names:
    if user_name == 'admin':
        print(
            f"Hello {user_name.title()}, would you like a status report today?")
    else:
        print(f"Hello {user_name.title()}, thank you for logging in today!")
