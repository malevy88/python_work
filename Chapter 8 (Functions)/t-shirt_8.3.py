# write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. the function should print a
# sentence summarizing the size of the shirt and the message printed on it.

# call the function once using positional arguments to make a shirt.
# call the function a second time using keyword arguments.


def make_shirt(size, text):
    """Display information about a shirt."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + text + '"')


make_shirt('XXXL', 'Hidden Characters')
make_shirt(size='XXXL', text='Hidden Characters')
