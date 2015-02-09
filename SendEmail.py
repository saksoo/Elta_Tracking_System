from datetime import datetime
import smtplib


def SendEmail(to_addr_list, cc_addr_list, subject, message):
  
  username = 'username'
  password = 'password'

  smtpserver = 'localhost'
  
  Sender = 'sender@mail'
  receivers_list = to_addr_list+cc_addr_list  

  header  = 'From: %s\n' % Sender
  header += 'To: %s\n' % ','.join(to_addr_list)
  header += 'Cc: %s\n' % ','.join(cc_addr_list)
  header += 'Subject: %s\n\n' % subject
  message = header + message

  try:
    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(Sender, receivers_list, message)
    server.quit()
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" : Successfully sent email")
  except SMTPException:
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" : Error!! Unable to send email")

receiver = ['receiver_list']
cc_receivers = ['Cc_list']
Subject = 'Coolpad news'
message = 'You track number has changed, check please'
SendEmail(receiver, cc_receivers, Subject, message) 

