# choose a color for the alien as you did in the last exercise and write an
# if-else chain. If the alien's color is green, print a statement that the
# player just earned 5 points for shooting the alien. If the alien's color isn't
# green, print statement that the player just earned 10 points.
# write one version of this program that rus the if block and another that runs
# the else block.

# runs the else block
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# runs the if block
alien_color = 'green'

if alien_color == 'green':
    print("\nYou just earned 5 points!")
else:
    print("You just earned 10 points!")
