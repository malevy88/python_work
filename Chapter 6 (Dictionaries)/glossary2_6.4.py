# Now that you know how to loop through a dictionary, clean up the code from 6.3
# by replacing your series of print() calls with a loop that runs through the
# dictionary's keys and values.
# When you're sure that your loops works, add five more Python therm to your
# glossary. When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    'Tuple': 'used to store mulitple items in a single variable (cant change)',
    'List': 'used to store multiple items in a single variable (can change)',
    'Variable': 'symbolic name that is a reference or pointer to an object',
    'F-Strings': 'embedded expressions inside string literals',
    'Comments': 'code lines that will not be executed',
    'Loop': 'repeating something over until a particular condition is met',
    'List Length': 'how to determine the length of a list',
    "Dictionary": 'data structure more generally known as associative array',

}

for word, definition in glossary.items():
    print(f"\nWord: {word}")
    print(f"Definition: {definition}")
