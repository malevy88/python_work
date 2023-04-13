# admission for anyone under age 4 is free.
# admission for anyone between 4 & 18 is $25.
# admission for anyone 18 or older is $40.

age = 12
if age < 4:
    print("Your admission is free!")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# more concise way of running last command
age = 30

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
