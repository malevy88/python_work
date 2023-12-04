# write a program that polls users about their dream vacation.
# write a prompt similar to if you could visit one place in the world, where
# would you go?
# include a block of code that prints the results of the poll.

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What is your dream vaction spot? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond (yes/no) ")
    if repeat == 'no':
        polling_active = False

    for name, response in responses.items():
        print(f"{name} would like to vaction at {response}.")
