"""
write a function that stores information about a car in a dictionary. the 
function should always receive a manufacturer and a model name. it should then 
accept an arbitrary number of keyword arguments. call the function with the 
required information and two other name-value pairs, such as a color or an 
optional feature. print the dictionary that's returned to make sure all the 
information was stored correctly.
"""


def car_info(manufacturer, model, **car_info):
    """store information about a car in a dictionary"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
