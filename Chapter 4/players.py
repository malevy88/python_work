#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #slices from index 0-2

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) #slices from index 1-3

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) #if first number omitted, starts at 0

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) #same as above, starts at index 2

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) #prints the same but negative value goes from end of list

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'tommy', 'jacob', 'sarah', 'lindsey']
print(players[2:7:2]) #3rd value indicates jumps between slices

#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team")
for player in players[:3]: #loops through first 3 players on the list
    print(player.title()) #prints their names, capitalized