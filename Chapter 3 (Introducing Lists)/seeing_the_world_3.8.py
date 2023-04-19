#think of at least 5 different places in the world you'd like to visit 
#store locations in a list. make sure list is not in alphabetical order
#print list in original order.
#use sorted() to print list in alphabetical order without modifying actual list
#use sorted() to print in reverse-alphabetical order without changing actual list
#use reverse() to change order of list. print to show list has changed
#user reverse to change list back to original order and print
#use sort() to change list to alphbetical order and print
#use sort() to store list as reverse-alphabetical order and print.

travel = ['japan', 'amsterdam', 'italy', 'united kingdom', 'france']
print(travel)

print(sorted(travel)) #prints list in alphabetical order without changing order of original list
print(travel)

travel.reverse() #reverses order of list (not alphabetical)
print(travel) #prints reversed list

travel.reverse() #reverses the list back to the original order
print(travel) #prints in original order again

travel.sort() #sorts list in alphabetical order
print(travel) #prints alphabetized list

travel.reverse() #sorts the list in reverse alphabetical order
print(travel) #prints reversed alphabetical list