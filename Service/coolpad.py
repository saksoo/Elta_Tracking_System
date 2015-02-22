from __future__ import print_function
import requests
import json



#returns the requested data
#in case of errors
    # returns "WN" if number is not valid
    # returns "ERROR" if there is a service error
    # returns "NE" if tracking number does not exist in elta system 


def getData(order_num):
    
    order = order_num
    
    #prepare request to the server
    url = 'http://www.elta-courier.gr/track.php'
    payload = { 'number': order }
    
    if (len(order_num)!=13):
        print ("Enter a valid number")
        return "WN"
    
    # handle the exception
    try:                                                                    
        r = requests.post(url, data=payload)
        #print (r.status_code)
        #print (r.content)
    except requests.exceptions.RequestException as e:     
        print (e)
        return "ERROR"
    
            
    #Send the request to the server and change encoding to utf-8
    #Store the response in a string and decode it
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
    
    if (this_order[order_number]['result'] == "wrong number"):
        return "NE"
    
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
         
    return order_number,order_changes,list_of_dates,list_of_status,list_of_places,list_of_times

    

       
        

