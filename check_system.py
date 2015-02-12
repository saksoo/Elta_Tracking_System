from __future__ import print_function
from tabulate import tabulate
from datetime import datetime
from coolpad import getData
from SendEmail import Send
import json
import os

#call getData fuction from coolpad
passed_data = getData("RF310279044SG")

#get list values
number   = passed_data[0]
changes  = passed_data[1]
dates    = passed_data[2]
status   = passed_data[3]
places   = passed_data[4]
times    = passed_data[5]

#for every status change make table and write 
#to status_list.txt
f = open('status_list.txt','w')
for i in range(changes):
  table = [[dates[i]],[times[i]],[status[i]],[places[i]]]
  t = tabulate(table)
  s = unicode(t)
  f.write(s.encode('utf-8'))  
f.close()

#get file size from old and new status files
statinfo = os.stat('status_list.txt')
file_size1 = statinfo.st_size

statinfo = os.stat('old_status_list.txt')
file_size2 = statinfo.st_size

#if size of new status file is bigger then
#sending email with the last change
if(file_size1 > file_size2):
  
  #decode json format
  u_times = unicode(times[changes-1])
  u_dates = unicode(dates[changes-1])
  u_status = unicode(status[changes-1])
  u_places = unicode(places[changes-1])
  
  #write new status in the old status file 
  f = open('old_status_list.txt','w')
  for i in range(changes):
    table = [[dates[i]],[times[i]],[status[i]],[places[i]]]
    t = tabulate(table)
    s = unicode(t)
    f.write(s.encode('utf-8'))
  f.close()
  
  #sending mail with the last change
  receivers = ['receiver@mail.com']
  cc_receivers = ['Cc_mail_list ']
  Subject = 'Coolpad news'
  message = 'You tracking number has changed:\n'+''.join(u_times.encode('utf-8'))+'\n'+''.join(u_dates.encode('utf-8'))+'\n'+''.join(u_status.encode('utf-8'))+'\n'+''.join(u_places.encode('utf-8'))
  
  Send(receivers, cc_receivers, Subject, message)
else:
  #write in log file
  print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": No status change")
  log = open('file.log','a')
  log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \nNo status chage \n\n")
  log.close()
  

