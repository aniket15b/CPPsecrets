from gmail_drafts import GMailDraftUser
import re
from email.mime.text import MIMEText
import base64
from message_maker import create_message, get_input

if __name__ == '__main__':
    sender, receiver, subject, body = get_input()
    user = GMailDraftUser()
    message = create_message(sender, receiver, subject, body)
    print(user.create_draft(message))