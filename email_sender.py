from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

load_dotenv()

email_sender = os.getenv("EMAIL_ADDR")
email_password = os.getenv("MAIL_KEY")

email_receiver = input('\nEnter Recipient Email Address: ')

subject = 'New Python Project'
body = """
Making a python script to send email.
"""

# making the emil insistance
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
print(f'\nEmail has been sent to: "{email_receiver}"')
