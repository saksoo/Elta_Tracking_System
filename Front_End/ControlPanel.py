from Service import coolpad
import tkinter
from tkinter import *
#import sys
#sys.path.append('..\Service')
#import coolpad





#Font for label text
#saksoofont = ('Times',15,"bold")


def TrackAction():
    
    #Clear all text
    output_text.delete("0.0",END)
    
    tracking_number = E1_text.get()

    #order = "RE422523075GR"
    
    data = coolpad.getData(tracking_number)
    
    if data == "ERROR":
        output_text.insert(INSERT, "Elta Service is not responding, Please try again later!\n")
        return
    elif data == "WN":
        output_text.insert(INSERT, "Please insert a valid number!\n")
        return
    elif data == "NE":
        output_text.insert(INSERT, "There is no entry for this tracking number!\n")
        return
    else:
        output_text.insert(INSERT, "Your tracking number is: \n") 
        output_text.insert(END, (data[0]) + "\n\n") 
        
        output_text.insert(END, "Tracking details: \n\n\n") 
        output_text.insert(END, "Date" + "\t" + "\t" + "Time" +  "\t" + "Status"+ "\t" + "\t" + "\t"+ "\t"+  "\t"+ "\t" +"Location\n") 
        
        
        order_changes = data[1]
        for i in range(0,order_changes):
            date     = data[2][i]
            status   = data[3][i]
            location = data[4][i]
            time     = data[5][i]
           
            output_text.insert(END, date + "\t" + "\t"+ time +  "\t" + status+  "\t"+ "\t" + "\t"+ "\t"+ "\t"+ "\t" + location + "\n") 
    
        return


def ClearAction():
    output_text.delete("0.0",END)



#Frame design_info
#Design the Frame
top = tkinter.Tk()

#background_image=PhotoImage(file="logo.gif")
#background_label = Label(top, image=background_image)
#background_label.place(x=220, y=90)


#Label for Intro
label_var = StringVar()
bulabel = Label( top,  textvariable=label_var, relief=RAISED, width= 120, height = 2 , fg = 'RED')
bulabel.pack()
label_var.set("Welcome to the Elta Tracking System: ")

#Label to create empty space
label2 = Label(top)
label2.pack()

#Entry text for the order
E1_text = StringVar()
E1 = tkinter.Entry(top, bd =5, textvariable=E1_text, width = 50)
E1.pack(side=TOP)
E1_text.set("Insert the tracking number: ")

#Label to create empty space
label3 = Label(top)
label3.pack()


output_text = Text(top, width = 100)
output_text.pack()

#Label to create empty space
label5 = Label(top)
label5.pack()



#Button for Track!!!!!
btn = tkinter.Button(top, text ="Track it!!!", bd = 9, command=TrackAction,  width="25", relief = RAISED)
btn.pack()

#Label to create empty space
label4 = Label(top)
label4.pack()


#Button for Clear text!!!!!
btnclr = tkinter.Button(top, text ="Clear", bd = 9, command=ClearAction,  width="25", relief = RAISED)
btnclr.pack()


#top.wm_iconbitmap('favicon.ico')
top.title("Elta Tracking - Control Panel")
top.mainloop()


