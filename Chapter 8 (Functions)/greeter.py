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
