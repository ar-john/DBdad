#!/usr/bin/python
import connector
import PartFinder
import PartPage
import AdminConsole
import UpdateExistingEmployee
import AdminPartUpdate
import tkinter as tk

#creates a db object
# mydb = connector.DB()



#this method is the from the command property in the submitBtn
#if login is good then user gets new window
def subLogin():
    #creates a db object
    mydb = connector.DB()
    if mydb.authLogin(username.get(), password.get()) == True:
        if mydb.chkAdmin(username.get()) == True:
            mydb.exit()
            root.destroy()
            window = tk.Toplevel(AdminConsole.AdminCon())
            window.transient(root)
            
        else:
            mydb.exit()
            root.destroy()
            window = tk.Toplevel(PartFinder.partWin())
            window.transient(root)
            
        
    else:
        print('wrong user or pass')
    # mydb.exit()

#test tkinter login page
root = tk.Tk()
root.geometry("300x300")
root.title("Login Page")

#defining first row
lbluser = tk.Label(root, text="Username - ")
lbluser.place(x = 50, y = 20)

username = tk.Entry(root, width=100)
username.place(x=150, y=20 , width=100)

#defining second row
lblpass = tk.Label(root, text="Password - ")
lblpass.place(x = 50, y = 50)

password = tk.Entry(root, width=35)
password.place(x = 150, y = 50 , width=100)

submitbtn = tk.Button(root, text='Login', bg='blue', command=subLogin)
submitbtn.place(x=150, y=135, width=55)

root.mainloop() #tested fine. command executes on button click




