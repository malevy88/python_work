# write a loop that prompts the user to enter a series of pizza toppings until
# they enter a 'quit' value. as the enter each topping, print a message saying
# you'll add that topping to their pizza.

prompt = "\nWhat kind of toppings do you want to add to your pizza?"
prompt += "\nEnter 'quit' to finish building your pizza. "

pizza = []
active = True
while active:
    toppings = input(prompt)

    if toppings == 'quit':
        active = False
    else:
        print(f"You can have {toppings} added to your pizza")
        pizza.append(toppings)

print(f"You've added {pizza} to your pizza!")
