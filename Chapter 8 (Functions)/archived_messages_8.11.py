"""
start with your work from exercise 8.10. Call the function send_messages() with
a copy of the list of messages. After calling the function, print both of your
lists to show that the original list has retained its messages.
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

send_messages(messages[:], sent_messages)
show_sent_messages(sent_messages)

print(messages)
print(sent_messages)
