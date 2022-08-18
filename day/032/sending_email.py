import ssl
import smtplib
from email.message import EmailMessage

with open("../../../passwords.txt") as passwords_data:
    email_password = passwords_data.readline()

email_sender = "wanzaz.contact@gmail.com"
email_receiver = "wanzaz.contact@yahoo.com"

subject = "Testing email connectivity"
body = "Hello!"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

# gmail = stmp.gmail.com, hotmail = smtp.live.com, yahoo = smtp.mail.yahoo.com
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
    connection.login(user=email_sender, password=email_password)
    connection.sendmail(from_addr=email_sender, to_addrs=email_receiver, msg=em.as_string())
    # msg="Subject:Hello\n\nThis is the body of the email"

