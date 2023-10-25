host_email = "k29263306@gmail.com"
recipient_email = "kaolin.stacey@gmail.com"

password = "bumsqpvbnmnmuljr"
email_host = "gmail.com"
email_port = "465"

import re

from time import sleep
from email.message import EmailMessage

import email
import smtplib
import imaplib

def sendEmail():
    subject = "Subject: FAN CONTROL"
    body = "Your home temperature is greater than 25. Do you wish to turn on the fan. Reply YES if so."
    em = EmailMessage()
    em['From'] = host_email
    em['To'] = recipient_email
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL(f'smtp.{email_host}') as server:
        server.connect("smtp.gmail.com",email_port)
        server.login(host_email, password)
        server.sendmail(host_email,recipient_email,em.as_string())


def receiveEmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')  
    mail.login(host_email, password)
    mail.select('inbox') 
    status, data = mail.search(None, 'All')
    mail_ids = []

    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i,'(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']

                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                
                print(f'From: {mail_from}')
                
                msg = mail_content.split('<')[0]
                print(f'Content: {msg}')

                if "yes" in msg.lower():
                    print('replied with yes')

if __name__ == "__main__":
    # sendEmail()
    receiveEmail()