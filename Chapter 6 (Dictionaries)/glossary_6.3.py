# think of 5 programming words you've learned about in a previous chapters.
# use these words as the keys in your glossary, and store their meanings as
# values.
# print each word and its meaning as neatly formatted output.
# you might print the word followed by a colon and then its meaning, or print
# the word on one line and then print its meaning indented on a second line.
# use the newline character to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'tuple': 'used to store mulitple items in a single variable (cant change)',
    'list': 'used to store multiple items in a single variable (can change)',
    'variable': 'symbolic name that is a reference or pointer to an object',
    'f-strings': 'embedded expressions inside string literals',
    'comments': 'code lines that will not be executed',
}

print(f"Tuple: {glossary['tuple']}.")
print(f"List: {glossary['list']}.")
print(f"Variable: {glossary['variable']}.")
print(f"F-Strings: {glossary['f-strings']}.")
print(f"Comments: {glossary['comments']}.")
