# modify the make_shirt() function so that shirts are large by default with a
# message that reads I love Python. Make a large shirt and a medium shirt with
# the default message, and a shirt of any size with a different message.

def make_shirt(size='large', text='I Love Python'):
    print(f"\nI have made you a {size} shirt.")
    print(f"It says {text}.")


make_shirt()
make_shirt(size='medium')
make_shirt(size='XXXL', text='I love Swift')
