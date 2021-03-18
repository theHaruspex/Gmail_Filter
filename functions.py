from configuration.config import service


def get_messages_list():
    """This function grabs all messages in your gmail inbox.
    Adapted from: https://github.com/imranm/Gmail-API-Read-All-Emails-Python """
    try:
        result = service.users().messages().list(userId='me', maxResults=500).execute()
        messages_list = []
        if 'messages' in result:
            messages_list.extend(result['messages'])

        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = service.users().messages().list(userId='me',
                                                     pageToken=page_token,
                                                     maxResults=500).execute()
            messages_list.extend(result['messages'])
            print('... total %d emails on next page [page token: %s], %d listed so far' % (
                len(result['messages']), page_token, len(messages_list)))
        return messages_list

    except Exception as error:
        print(f'An error occurred: {error}')


def message_to_trash(message):
    """This function moves the selected message to the trash folder and returns the message object."""
    while True:  # This function is prone to timeout, so it repeats until it succeeds.
        try:
            message_id = message['id']
            result = service.users().messages().trash(userId='me', id=message_id).execute()
            return result
        except Exception as error:
            print(f'Received error: {error}. Restarting.')
            continue


def get_message_sender(message):
    """This function returns the sender of a selected message."""
    while True:  # This function is prone to timeout, so it repeats until it succeeds.
        try:
            message_package = service.users().messages().get(userId='me', id=message['id']).execute()
            payload = message_package['payload']
            headers_list = payload['headers']
            for header in headers_list:
                if header['name'] == 'From':
                    sender = header['value']
                    return sender
        except Exception as error:
            print(f'Received error: {error}. Restarting.')
            continue
