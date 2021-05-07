#!/usr/bin/env python3

import smtplib as smtp
from getpass import getpass

email = input('введите почту: \n')
password = getpass('введите пароль: ')
dest_email = input('введите адрес получателя: \n')
subject = input('тема письма: \n')
email_text = input('текст письма: \n' )

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                       dest_email,
                                                       subject,
                                                       email_text)

server = smtp.SMTP_SSL('smtp.yandex.com', 465)
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()
