# returning a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('james', 'maynard')
print(musician)
