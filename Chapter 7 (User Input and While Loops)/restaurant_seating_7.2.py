# write a program that asks the user how many people are in their dinner group.
# if the answer is more than eight, print a message saying they'll have to wait
# for a table. otherwise, report that their table is ready.

reservation = input("How many people are going to be dining with us tonight? ")
reservation = int(reservation)

if reservation >= 8:
    print("Sorry but you'll have to wait to be seated.")
else:
    print("You can come with me. Your table is ready")
