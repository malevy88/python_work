# if statements
age = 19
if age >= 18:
    # prints both indented lines since true
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\n")

# if else statements
age = 17
# executes the else statement since age is only 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
