from datetime import datetime
import smtplib


def Send(to_addr_list, cc_addr_list, subject, message):
  
  #server username&password
  username = 'username'
  password = 'password'
  
  #smtp server domain
  smtpserver = 'localhost'
  
  Sender = 'your@mail.com'
  receivers_list = to_addr_list+cc_addr_list  
  
  #build email message
  header  = 'From: %s\n' % Sender
  header += 'To: %s\n' % ','.join(to_addr_list)
  header += 'Cc: %s\n' % ','.join(cc_addr_list)
  header += 'Subject: %s\n\n' % subject
  message = header + message

  try:
    
    #send mail
    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(Sender, receivers_list, message)
    server.quit()
    
    #write action to log file
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": Successfully sent email")
    log = open('file.log','a')
    log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \nStatus has chaged\nSuccessfully sent email\n\n")
    log.close()
  except SMTPException:
    #write action to log file
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \nError!! Unable to send email\n\n")
    log = open('file.log','a')
    log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \nError!! Unable to send email\n\n")
    log.close()

