import smtplib
import ssl


def send_email(email, message):
    host = "smtp.gmail.com"
    port = 465
    username = email
    password = "byzfpwtscxgcbqus"
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