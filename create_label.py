from gmail_label import GMailLabelUser

if __name__ == '__main__':
    print('Enter name of label :-')
    name = input()
    user = GMailLabelUser()
    label = user.create_label(name)
    