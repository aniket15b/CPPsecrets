from gmail_label import GMailLabelUser

if __name__ == '__main__':
    print('Enter name of label :-')
    label_name = input()
    user = GMailLabelUser()
    user.find_label(label_name)