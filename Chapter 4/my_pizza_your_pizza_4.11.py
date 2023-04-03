# start with program from 4.1. Mkae a copy of the list of the pizzas, and call it friend_pizzas. then do the following
# add a mew pizza to the original list
# add a different pizza to the list friend_pizzas
# prove you have 2 separate lists, print the message My favorite pizzas are; and then use a for loop to the print first list
# print the message My friend's favorite pizzas are; and then use a for list to print the second list
# make sure each new pizza is stored in the appropiate list

favorite_pizzas = ['sausage pizza', 'pepperoni pizza', 'cheese pizza']
print(favorite_pizzas)

friends_favorite_pizza = favorite_pizzas[:]
friends_favorite_pizza.append('hawaiian pizza')
print(friends_favorite_pizza)
print(favorite_pizzas)

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friends_favorite_pizza:
    print(friend_pizza)