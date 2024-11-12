#MAIL SENDING PROGRAM
"""The smtplib module define a smtp client session object that can be used to send mail to any internet machine
SMTP Stands for simple mail transfer protocol
the SMTPLIB module is use ful for communicating with mail server to send mail
Sending  mail is done with PYTHON programmming language module SMTPLIB"""

import smtplib
for server in range (1,Enter no of emails you want to send +1):
      server=smtplib.SMTP("smtp.gmail.com",587)                  
      server.starttls()
      server.login("sender email","app password")
      server.sendmail("sender email", "receiver email","Message you want to send")
print("Mail sent successfully")
