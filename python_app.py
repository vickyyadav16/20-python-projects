# go over to gmail account and setup 2 factor authentication,
# generate app password,
#create a fuction to send the mail.
from email.message import EmailMessage
from  app2 import password
import ssl
import smtplib

email_sender = 'amrvickyy@gmail.com'
email_password = password

email_receiver = 'focigi5895@anlubi.com'

subject = "Dont forget to Connect"
body = """
when you see my GitHub account,hit to connect
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

