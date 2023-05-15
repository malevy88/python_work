# write different versions of either 7-4 or 7-5 that does each of the following
# at least once.
# use a conditional test in the while statement to stop the loop
# use an active variable to control how long the loop runs.
# use a break statement to exit the loop when user enters a 'quit' value


# adding a break

prompt = "\nEnter you age to see how much the movies cost"
prompt += "\n(Entering 'quit' will exit the prompt.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    elif int(age) == 0:
        print("Please enter a valid age.")
    elif int(age) <= 3:
        print("\nYour ticket is free.")
    elif int(age) <= 12:
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")
