# write an if-elif-else chain that determines a person's stage in life
# set a value for the variable age and then:
# if person us under 2, print a that they're a baby
# if the person is at least 2 but less than 4, they're a toddler
# if at least 4 but less than 13, print they're a kid
# if at least 13 but less than 20, print theyre a teenager
# if person at least 20 but less than 65, print they're an adult
# if person 65 or older print they're an elder

age = 66

if age < 2:
    print("You're just a baby!")
elif age < 4:
    print("You're just a toddler!")
elif age < 13:
    print("You're just a kid!")
elif age < 20:
    print("You're just a teenager!")
elif age < 65:
    print("You're an adult now.")
else:
    print("You're an elder now")
