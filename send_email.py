import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "ggronnii@gmail.com"
password = "byzfpwtscxgcbqus"

receiver = "ggronnii@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Application Request
How are you? 
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)