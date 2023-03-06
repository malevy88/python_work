bicycles = ['trek', 'cannondale', 'redline', 'specailized']
print(bicycles) #prints the whole list
print(bicycles[0]) #prints just trek from list
print(bicycles[0].title()) #prints just trek from list but capitalized
print(bicycles[1]) #prints cannondale
print(bicycles[3]) #prints specialized
print(bicycles[-1]) #-1 always returns the last item in a list

message = f'My first bicycle was a {bicycles[0].title()}'
print(message)