#numerical comparisons

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("This is not the correct answer. Please try again!")

age = 19
print(age < 21) #returns true
print(age <= 21) #returns true
print(age > 21)  #returns false
print(age >= 21) #returns false

age_0 = 22
age_1 = 18

# both conditions have to be met with AND to return a true statement
print(age_0 >= 21 and age_1 >= 21) #returns false
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) #returns true

# one condition has to be met for OR condition to return true statement
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) #returns true

age_0 = 18
print(age_0 >= 21 or age_1 >= 21) #returns false