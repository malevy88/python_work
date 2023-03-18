squares = [] #start with empty list
for value in range(1, 11):
    square = value ** 2 #multiplies interger by itself 
    squares.append(square) #adds the square value to the end of the list
    print(squares) #prints the list

#more concise but temp variable from above is easier to read
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

#simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)