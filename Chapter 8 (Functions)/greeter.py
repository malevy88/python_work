def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# passing information to a function
# arguments and parameters


def greet_user(username):  # < username is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesse')  # < jesse is the argument

# using a function with a while loop


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# this stops the infinite loop below
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
