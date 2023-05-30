"""
write a function thart accepts a list of items a person wants on a sandwich. the
function should have one parameter that collectes as many item as the function
call provides, and it should print a summary of the sandiwches that's being 
ordered. call the function 3 times, using a different number of arguments each
time.
"""


def sandwiches(*toppings):
    print("\nMaking a sandwich with:")
    for topping in toppings:
        print(f"- {topping}")


sandwiches('mozzerella', 'pepperoni', 'spicy giardinara')
sandwiches('cheddar', 'turkey', 'pickles')
sandwiches('swiss', 'ham', 'lettuce')
