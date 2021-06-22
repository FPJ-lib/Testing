

'''
https://www.lynda.com/Python-tutorials/Send-email/2938119/2290769-4.html


Input:
receiver email
Adress
Subject line
Message Body
'''

import smtplib

SENDER_EMAIL = 'filipepessoajorge2@gmail.com'
SENDER_PASSWORD = 'pythontest1'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

#send_email('sebastiaofv@gmail.com', 'Sent with Python', 'So para o show-off ahah\n\nBye')


print('over')