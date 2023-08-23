import smtplib
import ssl
import os
from dotenv import load_dotenv


def main():
    password = os.getenv("PASSWORD")
    print(f"Password from environment variable: {password}")


def send_email(email, message):
    load_dotenv()
    host = "smtp.gmail.com"
    port = 465
    username = email
    password = os.getenv("PASSWORD")
    receiver = "ggronnii@gmail.com"
    context = ssl.create_default_context()
    message = f"""\
Subject: Application Request from {username}

From: {username}

{message}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(receiver, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    main()