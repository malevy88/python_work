# think of 5 programming words you've learned about in a previous chapters.
# use these words as the keys in your glossary, and store their meanings as
# values.
# print each word and its meaning as neatly formatted output.
# you might print the word followed by a colon and then its meaning, or print
# the word on one line and then print its meaning indented on a second line.
# use the newline character to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'Tuple': 'used to store mulitple items in a single variable (cant change)',
    'List': 'used to store multiple items in a single variable (can change)',
    'Variable': 'symbolic name that is a reference or pointer to an object',
    'F-Strings': 'embedded expressions inside string literals',
    'Comments': 'code lines that will not be executed',
}

print(f"Tuple: {glossary['Tuple']}. \n")
print(f"List: {glossary['List']}. \n")
print(f"Variable: {glossary['Variable']}. \n")
print(f"F-Strings: {glossary['F-Strings']}. \n")
print(f"Comments: {glossary['Comments']}. \n")

# added the second method (tab on second line)
for word, definition in glossary.items():
    print(f"\nWord: {word}")
    print(f"\tDefinition: {definition}")
