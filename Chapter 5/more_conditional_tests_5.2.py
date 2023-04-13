# test for equality and inequality with strings
# test using the lower() method
# numerical tests involving equality/inequality, greater than and less than,
# greater than or equal to, and less than or equal to
# tests using the and keyword and the or keyword
# test whether an item is in a list
# test whether an item is not in a list


full_name = 'marcus allen'
print('Is Marcus allen equal to marcus allen')
print(full_name == 'Marcus Allen')  # false since not capitalized
print("It appears that it isn't!")


print("\nWhat if we changed it to uppercase?")
new_full_name = full_name.title()  # changes it to capitalized
print(new_full_name == 'Marcus Allen')  # returns true
