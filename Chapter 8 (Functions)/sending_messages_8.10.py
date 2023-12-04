"""
start with a copy of your program from Exercise 8-9. Write a function called
send_messages() that prints each text message and moves each message to a new
list called sent_messages() that prints each message and moves each message to a
new list called sent_messages as its printed. After calling the function, print
both of your lists to make sure the messages were moved correctly.
"""

messages = ['hello', 'how are you?', 'what are you doing?', 'goodbye']
sent_messages = []


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages)
print("\nFinal lists:")
print(messages)
print(sent_messages)
