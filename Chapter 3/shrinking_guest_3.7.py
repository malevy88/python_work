#start with program from 3.6. Add a new line that print a message saying you can invite only two people for dinner.
#use pop() to remove guests from your list one at a time until only two names remain in your list. 
#for each pop, print a message to that person letting them know you're sorry ann have to un-invite them.
#print message to the two people still on your list letting them know they're still invited
#use del to remove the last two names so you have an empty list (print to make sure list is empty)

guest_list = ['Kobe Bryant', 'Michael Jordan', 'Giannis Antemkoupmo', 'Virgil Abloh', 'Jay Z']
guest_six = guest_list.insert(0, 'Phil Knight')
guest_seven = guest_list.insert(3, 'Gee Patta')
guest_eight = guest_list.append('Sandy Bodecker')
print(guest_list)
guest_pop_0 = guest_list.pop(0)
guest_pop_1 = guest_list.pop(1)
guest_pop_2 = guest_list.pop(2)
guest_pop_3 = guest_list.pop(3)
guest_pop_4 = guest_list.pop(3)
guest_pop_5 = guest_list.pop(1)


print("Hey everyone, it appears that the table won't come in time to have everyone over. I can only invite 2 of you now")
print(f"I'm sorry {guest_pop_0}, unfortunately I won't be able to have you over tonight.")
print(f"Apologies {guest_pop_1}, I won't be able to accomodate you this evening. Give the crew my regards")
print(f"Sorry {guest_pop_2}, I won't be able to have you over tonight. Let's reschedule for a different day!")
print(f"Sorry {guest_pop_3}, I won't be able to have you over tonight. Let's reschedule for a different day!")
print(f"Sorry {guest_pop_4}, I won't be able to have you over tonight. Let's reschedule for a different day!")
print(f"Sorry {guest_pop_5}, I won't be able to have you over tonight. Let's reschedule for a different day!")
print(f"Hey {guest_list[0]}, I'm glad that you can still make it to dinner tonight!") #Kobe's invitation
del guest_list[0] #deletes Kobe from list, making Virgil only one (0) left
print(f"{guest_list[0]}, I'm happy that you can still join us as well!") #virgil's invitation
del guest_list[0] #deletes Virgil from list, making list empty
print(guest_list) # print's empty list