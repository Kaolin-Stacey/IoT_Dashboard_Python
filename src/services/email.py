from datetime import datetime
from time import sleep
from email.message import EmailMessage

import email
import smtplib
import imaplib
import pytz


import config
from config import host_email, password, recipient_email

def sendEmail(msg):

    subject = "Subject: IoT Home"
    body = msg
    em = EmailMessage()
    em['From'] = host_email
    em['To'] = recipient_email
    em['Subject'] = subject
    em.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com') as server:

        server.connect("smtp.gmail.com","465")
        server.login(host_email, password)
        server.sendmail(host_email,recipient_email,em.as_string())


def receiveEmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')  
    mail.login(host_email, password)
    mail.select('inbox') 
    status, data = mail.search(None, 'ALL')
    mail_ids = []

    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i,'(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']

                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                
                date_str = message['date']
                email_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')

                if email_date > config.searchDate:
                    print(f'From: {mail_from}')
                    
                    if '<' in mail_content:
                        mail_content = mail_content.split('<')[0]
                        print(f'Content: {mail_content}')

                    if "yes" in mail_content.lower():
                        print('replied with yes')
                        import services.fan as fan
                        config.fanOn = True
                        fan.toggleFan()
                        return True
    return False


def checkTemperatureSendEmail():
    while(True):
        import config
        print("Waiting on reply: " + "yes" if config.waitingOnReply else "no")
        if config.fanOn or config.temperatureVal < config.temperatureThreshold or config.waitingOnReply: 
            sleep(5)
            continue

        config.waitingOnReply = True
        config.searchDate = datetime.now(pytz.UTC)

        sendEmail(f"Your home temperature is greater than {config.temperatureThreshold}. Do you wish to turn on the fan? Reply YES if so.")

        for i in range(60):
            if receiveEmail():
                break
            sleep(1)

        config.waitingOnReply = False
        
        sleep(900) # this will make the code wait 15 minutes before executing again