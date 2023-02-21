# Steps
# Go over to gmail account and setup 2 factor authentication
# Generate app password
# Create function to send the mail.
from app2 import key

from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'nabawangashadiah20@gmail.com'
email_key = key

email_receiver = 'nabawangashadiah20@gmail.com'

subject = 'Program'

body = """
Hope you are doing great, this is from my python program"""

# creating an instance of the EmailMessage package
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# setting a context for my mail
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_key)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    # the as_string converts the data in the EmailMessage instage as a string

