"""Use this file after get_senders_list.py, to filter out repeat senders
    while also prioritizing based on how many time a particular sender
    occurs in senders_list.txt.

    Note: If writing this again, I'd include this functionality in
    get_senders_list.oy"""

def occurrence(pair):
    """Used later as a sort function."""
    return pair[1]


with open('senders_list.txt', 'r') as txt_file:
    senders_list = [line[:-1] for line in txt_file.readlines()]

filtered_list = []
repeat_list = []
for sender in senders_list:
    if sender not in repeat_list:  # if a new sender, add it to both lists
        filtered_list.append([sender, 1])  # the integer keeps track of how many times the sender appears
        repeat_list.append(sender)
    elif sender in repeat_list:  # if not a new sender
        target_index = repeat_list.index(sender)  # determine the index of the sender in question in the lists
        (filtered_list[target_index])[1] += 1  # and raise the occurrence integer by one

filtered_list.sort(key=occurrence, reverse=True)  # sort the list


with open('filtered_list.txt', 'w') as txt_file:  # and save it
    for sender in [pair[0] for pair in filtered_list]:
        txt_file.write(sender + '\n')

