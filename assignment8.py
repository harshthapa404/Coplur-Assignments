#Assignment 8

#In this we use tkinter module that helps to use GUI

#With this we have to collect the data from the user GUI Based like Name,Email and Mobile Number and Store in a address_book.csv file.

import tkinter #It is a GUI(Graphical User Interface) module or library.

from tkinter import messagebox  #It means from tkinter get the messagebox function.

import csv      #It is also a module or library.(Comma Separated Value)


def address_book():

    name=entry1.get()       #Here we get the entry1 value in (name) variable
    email=entry2.get()      #Here we get the entry2 value in (email) variable
    mobile=entry3.get()     #Here we get the entry3 value in (mobile) variable

    l=[[name,email,mobile]]     #Here we create a list of the values that we get from user.

    with open("address_book.csv","a") as f:     #Now we open a csv file in (f) variable

        writer=csv.writer(f)                    #And we use csv.writer function to write in a open file (f).And store it in a (writer) variable

        for row in l:                           #Here (l) is a list and we are passing the value in a row one by one  
            writer.writerow(row)                #Here we call a function csv.writer() and with opened file (address_book.csv) that is stored in a variable (f)
                                                #And writerow() helps to write row that is coming from the (row) variable 

    messagebox.showinfo("Address book","Data uploaded successfully")        #This will show the popup messagebox with the message that you provide.




root=tkinter.Tk()           #Main application where the application start without this no window will appear
root.title("Upload Data in Address Book")       #This is the title of the window
root.geometry("500x500")                        #This is the width and height of the window



label1=tkinter.Label(root,text="Name of a User",font=("Arial",15)) #This is a label that we want to show
label1.pack(pady=20)                                               #This put the label in the window

entry1=tkinter.Entry(root,width=15,font=("Arial",15))               #This is a textbox we created
entry1.pack()                                                       #This will put the textbox in a window

label2=tkinter.Label(root,text="Email of a User",font=("Arial",15))
label2.pack(pady=20)

entry2=tkinter.Entry(root,width=15,font=("Arial",15))
entry2.pack()

label3=tkinter.Label(root,text="Mobile number",font=("Arial",15))
label3.pack(pady=20)

entry3=tkinter.Entry(root,width=15,font=("Arial",15))
entry3.pack()


label4=tkinter.Button(root,text="Submit Information", command=address_book,bg="grey")       #Here we created a label with some commands like what task we want to perform like
label4.pack(pady=10)                                                                        #in this we run a function address_book that helps to writes in csv file.



root.mainloop()                 #Here the application runs and keeps the window open until any action is done by user


   

        
