# return values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('james', 'maynard')
print(musician)

# Making an argument optional


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


# doesn't work without middle name
musician = get_formatted_name('james', 'herbert', 'maynard')
print(musician)

# works without middle name


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:  # if middle_name is not empty
        full_name = f"{first_name} {middle_name} {last_name}"
    else:  # if middle_name is empty
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('james', 'maynard')
print(musician)

musician = get_formatted_name('james', 'maynard', 'herbert')
print(musician)
