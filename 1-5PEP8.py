import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CONNECT_PARAMS = {
    'smpt': 'smtp.yandex.ru',
    'port': 25,
    'imap': 'imap.yandex.ru'
}

class MailBox:
    def __init__(self, connect_params, mail_address, password):
        self.smpt = connect_params['smpt']
        self.imap = connect_params['imap']
        self.port = connect_params['port']
        self.mail_address = mail_address
        self.password = password

    def send_mail(self, recipients, subject='', body=''):
        message = MIMEMultipart()
        message['From'] = self.mail_address
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(body))
        server = smtplib.SMTP(self.smpt)
        server.ehlo()
        server.starttls()
        server.login(self.mail_address, self.password)
        server.send_message(message)
        server.quit()

    def recieve_mail(self, header=None):
        reciever = imaplib.IMAP4_SSL(self.imap)
        reciever.login(self.mail_address, self.password)
        reciever.list()
        reciever.select("inbox")
        if header:
            criterion = f'(HEADER Subject "{header}")'
        else:
            criterion = 'ALL'
        result, data = reciever.uid('search', None, criterion)
        if data[0]:
            uid_list = data[0].split()
            latest_email_uid = uid_list[-1]
            result, data = reciever.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
        else:
            print('There are no letters with current header')
            email_message = None
        reciever.logout()
        return email_message


if __name__ == "__main__":
    test = MailBox(CONNECT_PARAMS, 'login@yandex.ru', "Password")
    test.send_mail(['login@gmail.com'], 'test', 'test')
    my_mail = test.recieve_mail()
    print(my_mail['Subject'])
