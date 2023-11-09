#Go to Google Account, Security & create an app password called Python, copy the password text & store it safely.

from email.message import EmailMessage
from email2 import password
from lorem_text import lorem
import ssl
import smtplib

plen = 2

email_sender = '' #insert sender's email
email_password = password #create a new py file and store password in variable for better security

email_receiver = '' #receiver's email address

subject = 'Coding email-sender project!'

body = """lorem ipsum dummy text
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
