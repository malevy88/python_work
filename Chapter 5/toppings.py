# checking for inequality

requested_topping = "mushrooms"

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
# true since mushrooms are on the list
print('mushrooms' in requested_toppings)
# false since pepperoni is not on the list
print('pepperoni' in requested_toppings)


# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# testing with if/elif argument
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
# doesn't get added since no in toppings list
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
# doesn't get added since argument for mushrooms passed, skipping over cheese
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
