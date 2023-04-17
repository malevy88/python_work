# turn your if-else chain from 5.4 into an if-elf chain.
# if the alien is green, print message that player earned 5 points
# if alien is yellow, player earned 10 points
# if alien red, player earned 15 points
# write 3 versions of this program, making sure each message is printed for the
# appropiate color alien

# 15 points
alien_color = "red"

if alien_color == "red":
    print("You just earned 15 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 5 points!")

# 10 points
alien_color = "yellow"

if alien_color == "red":
    print("You just earned 15 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 5 points!")

# 5 points
alien_color = "green"

if alien_color == "red":
    print("You just earned 15 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 5 points!")
