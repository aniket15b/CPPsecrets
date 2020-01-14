from gmail_reader import GMailReader

user = GMailReader()
listo = user.get_messages("from:aniket15b@gmail.com", length=4)
print([message['id'] for message in listo])