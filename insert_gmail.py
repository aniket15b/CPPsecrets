from gmail_inserter import GMailInserter
from message_maker import create_message, get_input

if __name__ == '__main__':
    sender, receiver, subject, body = get_input()
    user = GMailInserter()
    message = create_message(sender, receiver, subject, body)
    user.insert_mail(message)