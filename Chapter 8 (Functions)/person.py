# returning a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('james', 'maynard')
print(musician)

# stores a person's age as well


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('james', 'maynard', age=59)
print(musician)
