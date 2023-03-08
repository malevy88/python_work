#you just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
#start with your program from 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it.
#modify your list, replacing the name of the guest who can't make it with a name of the new person you are inviting.
#print a second set of invitation messages, one for each person who is still in your list

guest_list = ['Kobe Bryant', 'Michael Jordan', 'Giannis Antemkoupmo', 'Virgil Abloh', 'Jay Z']
cant_come = guest_list.pop(2)
new_guest_list = guest_list.append('Tinker Hatfield')
print(f"Unfortunately {cant_come} won't be able to make it to the dinner.")
print(f"I was wondering if {guest_list[0]}, {guest_list[1]}, and {guest_list[2]} had the opportunity to work with {guest_list[4]} before? Let's discuss over dinner.")
print(f"But don't worry {guest_list[3]}, you're still welcomed to dinner as well!")