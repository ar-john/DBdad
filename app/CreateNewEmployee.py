#!/usr/bin/python
import string
import tkinter as tk
import sys
import connector
import EmployeeAdministration

# import and init so we can use the database

def newEmp ():

    # mydb = connector.DB()
    createNewEmployee = tk.Tk()
    createNewEmployee.title("Create New Employee")
    createNewEmployee.geometry('350x200+50+50')


    def createEmployee():
        # emp = str(empId)
        # first = str(firstName)
        # last = str(lastName)
        # pas = str(password)
        # ad = str(admin)
        # newEmployee = []
        # newEmployee.append(emp)
        # newEmployee.append(first)
        # newEmployee.append(last)
        # newEmployee.append(ad)
        # newEmployee.append(pas)
        # print(newEmployee)
        # mydb.createEmp(newEmployee)
        # return newEmployee

        # newEmployee = []
        # newEmployee.append(employeeIdInput.get())
        # newEmployee.append(firstNameInput.get())
        # newEmployee.append(lastNameInput.get())
        # newEmployee.append(isAdmin.get())
        # newEmployee.append(passwordInput.get())
        mydb = connector.DB()
        mydb.createEmp(employeeIdInput.get(),firstNameInput.get(),lastNameInput.get(),isAdmin.get(),passwordInput.get())
        mydb.exit()



    employeeIdFrame = tk.Frame(createNewEmployee)
    employeeIdLabel = tk.Label(employeeIdFrame, text="New Employee ID: ")
    employeeIdLabel.pack(side=tk.LEFT)
    employeeIdInput = tk.Entry(employeeIdFrame, width=15)
    employeeIdInput.pack(side=tk.LEFT)
    employeeIdFrame.pack()

    firstNameFrame = tk.Frame(createNewEmployee)
    firstNameLabel = tk.Label(firstNameFrame, text="New Employee First Name: ")
    firstNameLabel.pack(side=tk.LEFT)
    firstNameInput = tk.Entry(firstNameFrame, width=15)
    firstNameInput.pack(side=tk.LEFT)
    firstNameFrame.pack()

    lastNameFrame = tk.Frame(createNewEmployee)
    lastNameLabel = tk.Label(lastNameFrame, text="New Employee Last Name: ")
    lastNameLabel.pack(side=tk.LEFT)
    lastNameInput = tk.Entry(lastNameFrame, width=15)
    lastNameInput.pack(side=tk.LEFT)
    lastNameFrame.pack()

    passwordFrame = tk.Frame(createNewEmployee)
    passwordLabel = tk.Label(passwordFrame, text="New Employee Password: ")
    passwordLabel.pack(side=tk.LEFT)
    passwordInput = tk.Entry(passwordFrame, width=15)
    passwordInput.pack(side=tk.LEFT)
    passwordFrame.pack()

    isAdmin = tk.BooleanVar()
    isAdminFrame = tk.Frame(createNewEmployee)
    isAdminCheck = tk.Checkbutton(isAdminFrame, text="Administrator", variable=isAdmin, onvalue=1, offvalue=0)
    isAdminCheck.pack()
    isAdminFrame.pack()

    # createButton = tk.Button(createNewEmployee, text="Create",
    #                         command=lambda:
    #                         createEmployee(employeeIdInput.get(1.0, "end-1c"),
    #                                         firstNameInput.get(1.0, "end-1c"),
    #                                         lastNameInput.get(1.0, "end-1c"),
    #                                         passwordInput.get(1.0, "end-1c"),
    #                                         isAdmin.get()))
    def back():
        createNewEmployee.destroy()
        window = tk.Toplevel(EmployeeAdministration.empAdmin())
        window.transient(createNewEmployee)

    # backButton = tk.Button(buttonFrame, text="Back", command=back)
    # backButton.pack(side = tk.RIGHT)
    # buttonFrame.pack()

    createButton = tk.Button(createNewEmployee, text="Create",command=createEmployee)
    createButton.pack(side=tk.RIGHT)
    createButton = tk.Button(createNewEmployee, text="Back", command=back)
    createButton.pack(side=tk.RIGHT)

    buttonFrame = tk.Frame(createNewEmployee)
    # createNewButton = tk.Button(createNewFrame, text="Create", command=createNew)

   
    def on_closing():
        sys.exit()

    createNewEmployee.protocol("WM_DELETE_WINDOW", on_closing)

    createNewEmployee.mainloop()
