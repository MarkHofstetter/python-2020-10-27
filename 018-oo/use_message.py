from message import Message, Email, SMS
from message.MessageSub.letter import Letter

# from message import SMS
'''
message = Message()
message.content = 'bla'
message.send()
'''

# sms ist ein Objekt der Klasse SMS

sms = SMS()
content = 'Hallo Body' # der inhalt kommt von "aussen" 
sms.content = content
sms.to = '+43123123'
sms.send()


email = Email()
email.content = 'Hallo Email Body'
email.subject = 'betreff'
email.to = 'bla@bli.at'
email.send()

letter = Letter()
letter.to = 'Adresse'
letter.content = 'Mein Brief'
print(letter.content)
print(letter.to)