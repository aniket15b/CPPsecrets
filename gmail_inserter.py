from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

class GMailInserter:
    def __init__(self):
        print('User Created')
        self.scopes = ['https://www.googleapis.com/auth/gmail.insert']
        creds = None
        if os.path.exists('token-insert.pickle'):
            with open('token-insert.pickle', 'rb') as token:
                creds = pickle.load(token)
        try:
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', self.scopes)
                    creds = flow.run_local_server(port=0)
                    with open('token-insert.pickle', 'wb') as token:
                        pickle.dump(creds, token)

            self.service = build('gmail', 'v1', credentials=creds)
        except Exception as error:
            print("Error occured while authenticating :-")
            print(error)
        print('GMail API auth completed')

    def insert_mail(self, message):
        """Directly inserts a message into only this user's mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

        Args:
        userId: string, The user's email address. The special value me can be used to indicate the authenticated user. (required)
        body: object, The request body.
            The object takes the form of an email message.

        Returns:
            An object in the form of an email message.
        """
        try:
            message = (self.service.users().messages().insert(userId='me', body=message).execute())
            print('Message Id: %s' % message['id'])
            return message
        except Exception as error:
            print('An error occurred while sending email: %s' % error)
            return None
