from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

message = MIMEMultipart()

template = Template(Path("template.html").read_text())

message["from"] = "Kamil Wójcik"
message["to"] = "kamil.jerzy.wojcik@gmail.com"
message["subject"] = "test send mail python"

body = template.substitute({"name": "John"})
body2 = template.substitute(name="John")

message.attach(MIMEText(body, "html"))

message.attach(MIMEImage(Path("dog.jpeg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("kamil.wojcik2008@gmail.com", "Sony20044")
    smtp.send_message(message)
    print("Sent...")