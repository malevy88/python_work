# writing clear prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# assigns the message to variable prompt
prompt = "If you share your name, we can personalize the message you see. "
# adds new string onto the end (on a second line)
prompt += "\nWhat is your first name? "
# passes prompt variable through name
name = input(prompt)
print(f"\nHello, {name}!")
