import smtplib    
sender_mail = 'jwang1122@gmail.com'    
receivers_mail = ['wangqianjiang@live.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   password = input('Enter the password: ');    #Qianjiang@1122
   smtpObj = smtplib.SMTP("gmail.com", 587)  
   smtpObj.login(sender_mail,password)     
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception as error:    
   print(error)
   print("Error: unable to send email")   

# telnet smtp.gmail.com 587