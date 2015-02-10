from __future__ import print_function
from tabulate import tabulate
import requests
import json



def getData(order_num):
    
    order = order_num
    
    #prepare request to the server
    url = 'http://www.elta-courier.gr/track.php'
    payload = { 'number': order }
    
    
    #Send the request to the server and change encoding to utf-8
    #Store the response in a string and decode it 
    r = requests.post(url, data=payload)
    r.encoding = 'utf-8'
    text = r.text
    response = json.loads(text)
    
    
    #For every order we find the order number
    #We keep the last number in our case, We have only one number
    for item in response['result']:
        order_number = item
    #print order_number
    
    
    #for this order
    this_order = response['result']
    
    #We keep lists with all the data of the order
    list_of_dates=[]
    list_of_status=[]
    list_of_places=[]
    list_of_times=[]
    
    
    
    #Find the changes of the order status
    order_changes = 0
    for item in this_order[order_number]['result']:
        order_changes+=1
    
    
    #Pushing the data to the lists
    for i in range(0,order_changes):
        list_of_dates.insert(i,this_order[order_number]['result'][i]['date'])     
        list_of_status.insert(i,this_order[order_number]['result'][i]['status'])  
        list_of_places.insert(i,this_order[order_number]['result'][i]['place'])
        list_of_times.insert(i,this_order[order_number]['result'][i]['time'])    
    
    
    #Printing the data
    #for i in range(0, order_changes):    
        #print  (list_of_status[i], list_of_dates[i], list_of_times[i] ,list_of_places[i])


        
    return order_number,order_changes,list_of_dates,list_of_status,list_of_places,list_of_times

passed_data = getData("RF310279044SG")

#Testing the values

number   = passed_data[0]
changes  = passed_data[1]
dates    = passed_data[2]
status   = passed_data[3]
places   = passed_data[4]
times    = passed_data[5]


f = open('status_list.txt','w')
for i in range(changes):
  table = [[dates[i]],[times[i]],[status[i]],[places[i]]]
  t = tabulate(table,headers = [" "])
  s = unicode(t)
  f.write(s.encode('utf-8'))
  
f.close()

print (number)
print (changes)
print (dates)
print (status[2])
print (places)
print (times)

print (places[1])





