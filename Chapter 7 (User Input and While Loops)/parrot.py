# how the input function works

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# while loop in action
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "  # letting use choose to quit

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# using a flag
