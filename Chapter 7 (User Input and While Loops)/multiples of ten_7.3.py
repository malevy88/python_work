# ask the user for a number, and then report whether the number is a multiple of
# 10 or not.

prompt = input("Enter a number to see if it is a multiple of 10! ")
prompt = int(prompt)

if prompt % 10 == 0:
    print(f"\nYes, {prompt} is a multiple of 10!")
else:
    print(f"\nNope, that number is not a multiple of 10!")
