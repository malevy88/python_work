# test for equality and inequality with strings ✅
# test using the title() method ✅
# numerical tests involving equality/inequality, greater than and less than,
# greater than or equal to, and less than or equal to
# tests using the AND keyword and the OR keyword
# test whether an item is in a list
# test whether an item is not in a list

# string and title example
full_name = 'marcus allen'
print('Is Marcus Allen equal to marcus allen')
print(full_name == 'Marcus Allen')  # false since not capitalized
print("It appears that it isn't!")
print("\nWhat if we changed it to uppercase?")
new_full_name = full_name.title()  # changes it to capitalized
print(new_full_name == 'Marcus Allen')  # returns true

# greater than or equal to example
age_0 = 35
age_1 = 36
print("\nWhat will 35 >= 36 result as? True or false")
print(age_0 >= age_1)
print("What about reversed? 35 <= 36?")
print(age_0 <= age_1)
