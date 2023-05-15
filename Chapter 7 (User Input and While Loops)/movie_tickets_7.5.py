# a movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free.
# if they are between 3-12, the ticket is $10.
# if over 12, the ticket is $15.
# write a loop in which you ask user's their age, and then tell them the cost
# of their movie ticket.

prompt = "\nEnter you age to see how much the movies cost"
prompt += "\n(Entering 'quit' will exit the prompt.) "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    elif int(age) <= 3:
        print("\nYour ticket is free.")
    elif int(age) <= 12:
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")
