"""
start with a copy of your program from Exercise 8-9. Write a function called
send_messages() that prints each text message and moves each message to a new
list called sent_messages() that prints each message and moves each message to a
new list called sent_messages as its printed. After calling the function, print
both of your lists to make sure the messages were moved correctly.
"""


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)


messages = ['hello', 'how are you?', 'what are you doing?', 'goodbye']
sent_messages = []

send_messages(messages, sent_messages)
show_sent_messages(sent_messages)
