from gmail_sender import GMailSender
from message_maker import create_message, get_input

if __name__ == '__main__':
    sender, receiver, subject, body = get_input()
    user = GMailSender()
    message = create_message(sender, receiver, subject, body)
    print(user.send_mail(message))