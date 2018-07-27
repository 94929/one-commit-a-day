#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

from extractor import Extractor
from config import gmail_username
from config import gmail_password


def send_mail(sender, recipient, text):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(sender, gmail_password)

    msg = MIMEText(text)
    msg['Subject'] = 'Daily commit notification regarding your Github account'

    smtp.sendmail(sender, recipient, msg.as_string())
    smtp.quit()


def notify_me(recipient):
    """ sends me an email saying that I might miss a commit for today """
    
    sender = gmail_username + '@gmail.com'
    msg = "You don't have any pushed commit today!"
    send_mail(sender, recipient, msg)


def has_valid_event():
    """ checks if there is a push event created by me today """
    
    return len(Extractor().events) != 0


def main():
    # do nothing if there is a pushed commit today
    if has_valid_event():
        return 

    # email me
    notify_me(Extractor().email)

    
if __name__ == '__main__':
    main()

