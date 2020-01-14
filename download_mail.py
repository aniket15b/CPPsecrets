from gmail_reader import GMailReader
import base64

if __name__ == '__main__':
    reader = GMailReader()
    print('Enter query to search message by :-')
    query = input()
    message = reader.get_single_message(query)
    message_decoded = base64.b64decode(message['raw']+'===')
    print('Enter name of file to save the message to :-')
    fname = input()
    with open(fname,'wb') as f:
        f.write(message_decoded)
    print('File downloaded')