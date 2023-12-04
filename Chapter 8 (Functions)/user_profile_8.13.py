"""
start with a copy of user_profile.py. Build a profile of yourself by calling 
build.profile() using your first and last names and three other key-value pairs
that describe you
"""


def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('marcus', 'levy', location='milwaukee',
                             field='information technology',
                             career_goal='Cloud Engineer')

print(user_profile)
