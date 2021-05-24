import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
receivers = ["jwang1122@gmail.com","wangqianjiang@live.com"]
sender = "jwang1122@gmail.com"
password = "Qianjiang@1122"
message = """
From: From Person <wangqianjiang@live.com>
To: To Person <jwang1122@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message
"""
# Create a secure SSL context
context = ssl.create_default_context()
# smtpObj = smtplib.SMTP(''smtp.gmail.com', 587')
smtpObj = smtplib.SMTP('localhost')

# Try to log in to server and send email
try:
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully send email")
except Exception as e:
    # Print any error messages to stdout
    print("Error: ",e)
finally:
    smtpObj.quit() 