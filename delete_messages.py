"""Use this file after you've composed a blacklist.txt from filtered_list.txt
    by going in and removing any sender that you want to keep messages from
    in your inbox."""

import os
from functions import *


with open('blacklist.txt', 'r') as txt_file:  # import the blacklist
    blacklist = [line[:-1] for line in txt_file.readlines()]

messages_list = get_messages_list()
message_senders_list = []  # get another list of all senders to later compare to blacklist
for i, message in enumerate(messages_list):
    print(f'{i} of {len(messages_list)}')
    message_senders_list.append(get_message_sender(message))


for i, message in enumerate(messages_list):  # iterating over all messages
    print(f'{i} of {len(messages_list)}')
    for blocked_sender in blacklist:
        message_sender = message_senders_list[i]
        if blocked_sender == message_sender:  # if the message sender is in the blacklist
            message_to_trash(message)  # delete the message

os.system('say process complete')
