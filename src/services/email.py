from time import sleep
from email.message import EmailMessage

import email
import smtplib
import imaplib

def sendEmail():
    global sender_email, recipient_email, password, email_host, email_port, awaitingResponse

    subject = "Subject: FAN CONTROL"
    body = "Your home temperature is greater than 25. Do you wish to turn on the fan. Reply YES if so."
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = recipient_email
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL(f'smtp.{email_host}') as server:
        server.connect("smtp.gmail.com",email_port)
        server.login(sender_email, password)
        server.sendmail(sender_email,recipient_email,em.as_string())

def receiveEmail():
    global awaitingResponse, sender_email, password, email_host
    for i in range(30):
        with imaplib.IMAP4_SSL(f'imap.{email_host}') as server:
            server.login(sender_email,password)
            server.select('inbox')
            status, data = server.search(None,"ALL")
            print('waiting for response')
            mail_ids = []

            for block in data:
                mail_ids += block.split()
            for i in mail_ids:
                status, data = server.fetch(i,'(RFC822)')

                for response_part in data:
                    if isinstance(response_part, tuple):
                        message = email.message_from_bytes(response_part[1])
                        mail_from = message["from"]
                        if recipient_email.lower() in mail_from.lower():
                            if message.is_multipart():
                                mail_content = ''

                                for part in message.get_payload():

                                    if part.get_content_type() == 'text/plain':
                                        mail_content += part.get_payload()
                            else:
                                mail_content = message.get_payload()
                                print(mail_content.lower())
                                if "yes" in mail_content.lower():
                                    print('response yes')
                                    return True
        sleep(1)