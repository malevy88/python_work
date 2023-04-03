# all versions of the foods.py in this section have avoided using for loops when printing, to save space.
# choose a versions of foods.py and write 2 for loops to print each list of foods

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli') 
friend_foods.append('ice cream')

print("My favorites foods by far are:")
for foods in my_foods:
    print(foods)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)