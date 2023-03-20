#a number raised to the third power is called a cube. 
#for example, the cube of 2 is written 2**3 in python.
#make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10)
#use a for loop to print out the value of each cube.

cube = []
for value in range(1, 11):
    cube = value ** 3
    print(cube)
