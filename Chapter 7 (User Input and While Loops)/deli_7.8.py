# make a list called sandwich_orders and fill it with the names of various
# sandiwches.
# then make an empty list called finished_sandwiches.
# loop through the list of sandwich orders and print a message for each order,
# such as "I made your tune sandwich."
# as each sandwich is made, move it to the list of finished sandwiches.
# after all the sandwiches have been made, print a message listing each sandwich
# that was made.

sandwich_orders = ['BLT', 'Philly Cheese Steak', 'Lobster Roll', 'Hot Ham']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
