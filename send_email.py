import smtplib, ssl, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("sender_email")
    password = os.getenv("password")
    receiver = os.getenv("receiver_email")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)