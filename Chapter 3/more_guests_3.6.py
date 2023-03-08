#you just found a bigger dinner table, so now more space is available. think of three more guests to invite to dinner.
#start with program from 3.4/3.5. Add a print() call to the end of your program, informing people that you found a bigger table. 
#use insert to add one new guest to the beginning of the list
#use insert to add one new guest to middle
#use append to add one new guest to the end 
#print a new set of invitation messages, one for each person in your list

guest_list = ['Kobe Bryant', 'Michael Jordan', 'Giannis Antemkoupmo', 'Virgil Abloh', 'Jay Z']
print("Hey everyone, we were able to get more people invited to the dinner party. Some of them you may know, some you may be meeting for the first time!")
guest_six = guest_list.insert(0, 'Phil Knight')
guest_seven = guest_list.insert(3, 'Gee Patta')
guest_eight = guest_list.append('Sandy Bodecker')

print(f"Thanks for making it tonight {guest_list[0]}. The company wouldn't be what it is without you!")
print(f"{guest_list[1]}, I know how busy your schedule is as well. I'm glad that you were still able to make it!!")
print(f"It wouldn't be a Nike party without {guest_list[2]} being here. Cheers!")
print(f"{guest_list[3]}, your Airmax 1 collection has to be so sick. Thanks for coming as well!")
print(f"Probably the newest addition to Nike, I'm glad you're here {guest_list[4]}.")
print(f"{guest_list[5]}, did you and {guest_list[0]} work closely together in your work with Nike?")
print(f"{guest_list[6]}, how big of a role were you in the Roc A Fella Air Force 1 creation?")
print(f"{guest_list[7]}, how does it feel knowing the impact that you made on the whole team at Nike?")