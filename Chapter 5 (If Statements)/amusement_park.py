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

# adding in a discount for seniors
age = 80

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# omitting the else block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}")
