from gmail_label import GMailLabelUser
from gmail_reader import GMailReader
from gmail_modifier import GMailModifier

if __name__ == '__main__':
    print('Enter query to search the message by :-')
    query = input()
    print('Enter number of messages matching the query to search for :- (Enter 0 for all messages)')
    num = int(input())
    if not num:
        lng = num
    else:
        lng = None
    reader = GMailReader()
    messages = reader.get_messages(query, length=lng)
    messageids = [message['id'] for message in messages]

    if not messages:
        print('No messages were found matching the given query.')
    else:
        labeluser = GMailLabelUser()
        modifier = GMailModifier()
        count = len(messages)
        print('Add the same label to all the messages? (yes/no)')
        switch = input()
        
        if(switch == 'y' or switch == 'yes'):
            print('Enter the name of label to attach :-')
            name = input()
            labelid = labeluser.find_labelid(name)
            labelids = [labelid for i in messages]
            modifier.add_labels(messageids, labelids)
        else:
            print('Enter name of %s no. of labels :-' % len(messages))
            labels = [input() for i in messages]
            labelids = [labeluser.find_labelid(labelname) for labelname in labels]
            modifier.add_labels(messageids, labelids)
