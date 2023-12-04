# Tuples
# like lists but cannot change list of items

dimensions = (200, 50)  # tuples use parenthesis instead of sqauare brackets
print(dimensions[0])  # can access indivdual items using indexes, like list
print(dimensions[1])

"""
changing a value in a tuple
dimensions = (200, 50) #declares dimension tuple
dimensions[0] = 250 #reassigns 0 index to 250
print(dimensions) #error out since we can't change the tuple
"""

# looping through a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# writing over a tuple
dimensions = (200, 50)
print('\nOriginal dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)  # re-assigns the whole dimension variable
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
