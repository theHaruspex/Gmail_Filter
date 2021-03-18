"""Use this file to compose and save a list of the senders
    of each email in your inbox."""

import os
from functions import *

messages_list = get_messages_list()
senders_list = []

for i, message in enumerate(messages_list):
    sender = get_message_sender(message)
    senders_list.append(sender)
    print(f'{i}: {sender}')
    print()

with open('senders_list.txt', 'w') as txt_file:
    for sender in senders_list:
        txt_file.write(sender + '\n')

os.system('say process complete')
