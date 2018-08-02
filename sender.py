from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from config import email_id
from config import email_pw


class Sender:
    """ This class sends an email to a given recipient regarding Github info 
    
    """

    def __init__(self, receiver):
        self.__sender = email_id
        self.__receiver = receiver
        self.__msg = self.__init_msg()
        
    def __init_msg(self):
        content = """ You don't have any pushed commit today! """

        msg = MIMEText(content)
        msg['Subject'] = "Daily commit notification on your Github account"
        return msg

    def send(self):
        smtp = SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(self.__sender, email_pw)
        smtp.sendmail(self.__sender, self.__receiver, self.__msg.as_string())
        smtp.quit()

