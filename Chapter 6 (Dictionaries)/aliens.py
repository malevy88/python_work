# a list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]  # the list of dictionaires

for alien in aliens:
    print(alien)

# more realistic example

# make an empty list for storing aliens
aliens = []

# make 30 green aliens.
for alien_number in range(30):  # returns 30 (repeats 30 times)
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}  # creates new
    aliens.append(new_alien)

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
