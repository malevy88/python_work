#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake'] #creates list of favorite foods
friend_foods = my_foods[:] #creates a copy by omitting first and last index

my_foods.append('cannoli') #appends cannoli to my foods list
friend_foods.append('ice cream') #appends ice cream to friends food list

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)