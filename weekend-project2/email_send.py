import sys
import smtplib
import logging

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def access_credentials():
    destination = 'config'
    username = ''
    password = ''
    recipient = ''
    credentials = []

    try:
        file = open(destination, 'r')
        logging.info(f'Checked file - {destination}')
    except:
        logging.error(f'Could not open file - {destination}')

    try:
        credentials = file.readlines()
        credentials = list(map(lambda f: f.rstrip('\n'), credentials))

        username = credentials[0]
        password = credentials[1]
        recipient = credentials[2]

        logging.info(f'Read from file - {destination}')
    except:
        logging.error(f'Could not read file - {destination}')
    
    try:
        file.close()
        logging.info(f'Closed file - {destination}')
    except:
        logging.error(f'Could not close file - {destination}')

    if username == '' or password == '':
        raise Exception('Credentials not found')

    return (username, password, recipient)

def send_email():
    username = ''
    password = ''
    recipient = ''

    try:
        credentials = access_credentials()
        
        username = credentials[0]
        password = credentials[1]
        recipient = credentials[2]
    except Exception as e:
        logging.error(f'Credentials error - {e}')
        raise Exception('Credentials error')

    # Start session, encryption, login
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(username, password)
    except:
        logging.error('Could not start session')
        raise Exception('Session start error')

    # Set header and main message body
    try: 
        msg = MIMEMultipart()
        msg['Subject'] = 'Weekend Project 2'
        msg['From'] = username
        msg['To'] = recipient

        text ='Hello,\n\nAttached is the Weekend Project 2 log file, plot 1, and plot 2.\n\nBest regards,\nStudent'
        msg.attach(MIMEText(text))
    except:
        logging.error('Could not create main message')
        raise Exception('Message creation error')

    # Attach log file
    try:
        filenames = ['weekend-project2.log', 'plot1.png', 'plot2.png']
        for f in filenames:
            with open(f, "rb") as file: 
                ext = f.split('.')[-1:]
                attachedfile = MIMEApplication(file.read(), _subtype = ext)
                attachedfile.add_header(
                    'content-disposition', 'attachment', filename=f)
            msg.attach(attachedfile)
    except:
        logging.error('Could not attach file')
        raise Exception('Message attachment error')

    # Send
    try:
        session.sendmail(username, recipient, msg.as_string())
        logging.info(f'Email sent to {recipient}')
    except:
        logging.error('Could not send message')
        raise Exception('Message send error')

    try:
        session.quit()
    except:
        logging.error('Could not end session')
        raise Exception('Session stop error')