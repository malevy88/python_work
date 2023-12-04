# modify your program from 6.2 so each person can have more than one favorite
# number. then print each person's name along their favorite numbers

favorite_numbers = {
    'Deandre': [5, 23],
    'Marcus': [00, 45],
    'Lindsey': [24, 88],
    'Amanda P': [4, 75],
    'Angus': [100, 1],
}

for name, favorite_number in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in favorite_number:
        print(f"{number}")
