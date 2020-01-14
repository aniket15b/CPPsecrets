from gmail_deleter import GMailDeleter

if __name__ == '__main__':
    print('Enter message id of the message to be deleted :-')
    message_id = input()
    user = GMailDeleter()
    user.delete_message(message_id)