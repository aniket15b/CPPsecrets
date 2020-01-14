from gmail_sender import GMailSender
from message_maker import create_message_with_attachment, get_input

if __name__ == '__main__':
    sender, receiver, subject, body, filepath = get_input()
    user = GMailSender()
    try:
        message = create_message_with_attachment(sender, receiver, subject, body, filepath)
    except Exception as error:
        print(error)
        message = create_message(sender, receiver, subject, body)
    print(user.send_mail(message))