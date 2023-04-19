#write a program that creates a list containing these items and then uses each function introduced in this chapter at least once

favorite_shoes = ['air max 1', 'air max 90', 'jordan 3', 'nike dunk low sb', 'jordan 4']

print(len(favorite_shoes)) #prints len()
print(sorted(favorite_shoes)) #prints sorted (alphabetical) list

favorite_shoes.reverse() #revereses list order
print(favorite_shoes) #prints reveresed order

favorite_shoes.reverse() #reverese list back to original order
print(favorite_shoes) #prints list in original order

print(favorite_shoes[1]) #prints second item in list

print(f"My favorite shoe of all time is {favorite_shoes[0].title()}.") #uses individual value from list

favorite_shoes[4] = 'air max 97' #replaces jordan 4 at end of list
print(favorite_shoes)

favorite_shoes.append('jordan 4') #adds jordan 4 back to the end of list
print(favorite_shoes)

favorite_shoes.insert(0, 'van authentics') #inserts vans authentics into first spot of list
print(favorite_shoes)

del favorite_shoes[0] #deletes vans from list
print(favorite_shoes)

first_owned = favorite_shoes.pop(0) #pops air max 1 from list
print(f"My first owned pair was {first_owned}")

favorite_shoes.remove('jordan 4') #removes jordan 4 from list
print(favorite_shoes)