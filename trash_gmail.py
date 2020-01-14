from gmail_modifier import GMailModifier

if __name__ == '__main__':
    print('Enter message id of the message to be deleted :-')
    message_id = input()
    user = GMailModifier()
    user.trash_message(message_id)