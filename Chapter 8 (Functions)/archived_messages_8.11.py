"""
start with your work from exercise 8.10. Call the function send_messages() with
a copy of the list of messages. After calling the function, print both of your
lists to show that the original list has retained its messages.
"""

messages = ['hello', 'how are you?', 'what are you doing?', 'goodbye']
sent_messages = []


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages[:])
print("\nFinal lists:")
print(messages)
print(sent_messages)
