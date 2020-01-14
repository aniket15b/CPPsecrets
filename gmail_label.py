from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

class GMailLabelUser:
    def __init__(self):
        print('User Created')
        self.scopes = ['https://www.googleapis.com/auth/gmail.labels']
        creds = None
        if os.path.exists('token-label.pickle'):
            with open('token-label.pickle', 'rb') as token:
                creds = pickle.load(token)
        try:
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', self.scopes)
                    creds = flow.run_local_server(port=0)
                    with open('token-label.pickle', 'wb') as token:
                        pickle.dump(creds, token)
            self.service = build('gmail', 'v1', credentials=creds)
        except Exception as error:
            print("Error occured while authenticating :-")
            print(error)
        print('GMail API auth completed')
    
    def create_label(self, label_name):
        label_obj = {'name': label_name}
        try:
            label = self.service.users().labels().create(userId='me', body=label_obj).execute()
            print('Label with id: %s created' % label['id'])
            return label
        except Exception as error:
            print('An error occurred while creating label: %s' % error)
            return None

    def find_labelid(self, name):
        try:
            obj = self.service.users().labels().list(userId='me').execute()
            names = [label['name'] for label in obj['labels']]
            labelids = [label['id'] for label in obj['labels']]
            if name in names:
                print('Found label: %s with labelid: %s' % (name, labelids[names.index(name)]))
            else:
                print('Label with name: %s not found' % (name))
            return labelids[names.index(name)]
        except Exception as error:
            print('An error occurred while creating label: %s' % error)
            return None