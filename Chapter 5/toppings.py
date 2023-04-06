# checking for inequality

requested_topping = "mushrooms"

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


# checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
#true since mushrooms are on the list
print('mushrooms' in requested_toppings) 
#false since pepperoni is not on the list
print('pepperoni' in requested_toppings)