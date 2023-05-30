""" 
make a list containing a series of short text messages. Pass the list to a 
function called show_messages(), which prints each text message.
"""

messages = ['hello', 'how are you?', 'what are you doing?', 'goodbye']


def show_messages(messages):
    print("Here are the messages:")
    for message in messages:
        print(message)


show_messages(messages)
