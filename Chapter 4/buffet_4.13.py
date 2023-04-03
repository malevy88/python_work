# a buffet style restuarant offers only five basic foods. think of five basic 
# foods and store them in a tuple.

# use a for loop to print each food the restaurant offers. try to modify one of 
# the items and make sure that Python rejects the change.

# the restaurant changes its menu, replacing two of the items with different 
# foods. add a line that rewrites the tuple, then use a for loop
# to print each of the item on the revised menu

buffet_menus = ("hot dog", "pizza", "chicken tenders", "buttered noodles", "chicken noodle soup", "fries")
print("This is going to be the Winter menu:")
for buffet in buffet_menus:
    print(buffet)

"""
buffet_menu[0] = "salad"
print(buffet_menu) #gets rejected since can't change a tuple item
"""

buffet_menus = ("salad", "pizza", "hamburger", "buttered noodles", "chicken noodle soup", "fries")
print("\nThis is going to be the Spring menu:")
for buffet in buffet_menus:
    print(buffet)
