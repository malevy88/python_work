# using the list sandwich_orders from 7.8, make sure the sandwich 'pastrami'
# appears in the list at least 3 times. Add code near the beginning of your
# program to print a message saying the deli has run out of pastrami, and then
# use a while loop to remove all occurenences of 'pastrami' from sandwich_orders.
# make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami', 'philly cheese streak', 'pastrami',
                   'cold cut trio', 'pastrami', 'blt', 'vegan']
finished_sandwiches = []

print("Sorry, we are all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"\nI made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
