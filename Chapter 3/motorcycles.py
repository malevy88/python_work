#MODIFYING ELEMENTS IN A LIST
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#APPENDING ELEMENTS TO THE END OF THE LIST
motorcycles.append('ducati') # adds ducati to the end of list
print(motorcycles)

motorcycles = [] # creates empty list and adds the following to list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#INSERTING ELEMENTS INTO A LIST
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') #inserts ducati in the first (0) spot
print(motorcycles)

#REMOVING AN ITEM USING THE DEL STATEMENT
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #deletes honda from list (0), used if you know position of item
print(motorcycles)

#REMOVING AN ITEM USING THE POP() METHOD
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcyles = motorcycles.pop() #pops out last variable in list (suzuki) and assigns it to popped_motorcyles
print(motorcycles)
print(popped_motorcyles)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop() #pops out suzuki and assigns it to last_owned
print(f"The last motorcycle that I owned was a {last_owned.title()}")

#POPPING ITEMS FROM ANY POSITION
first_owned = motorcycles.pop(0) #pops out Honda from the list and assigns it to first_owned
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#use del when you won't want to use the item from the list anymore. use pop when you will want to

#REMOVING ITEM BY VALUE
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati') #removes ducati item from list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")