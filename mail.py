from datetime import datetime
import requests
import smtplib
import os


def sendEmail():

  sender = 'sender@email.com'
  receivers = ['receiver@email.com']

  username = 'username'
  password = 'password'
  test = 'your test message'
    
  message = """From: From Person <from@fromdomain.com>
  To: To Person <receiver@email.com>
  Subject: Coolpad news
  """+test+"""
  Check Coolpad status...
  It's near!!!""" 
  
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login(username,password)
  smtpObj.sendmail(sender, receivers, message) 
  print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" : Successfully sent email")

sendEmail()
