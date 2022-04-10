import tkinter as tk

import connector

# import and init so we can use the database
mydb = connector.DB()

createNewEmployee = tk.Tk()
createNewEmployee.title("Create New Employee")
createNewEmployee.geometry('350x200+50+50')


def createEmployee(empId, firstName, lastName, password, admin):
    newEmployee = []
    newEmployee.append(empId)
    newEmployee.append(firstName)
    newEmployee.append(lastName)
    newEmployee.append(admin)
    newEmployee.append(password)
    print(newEmployee)
    return newEmployee


def back():
    return


employeeIdFrame = tk.Frame(createNewEmployee)
employeeIdLabel = tk.Label(employeeIdFrame, text="New Employee ID: ")
employeeIdLabel.pack(side=tk.LEFT)
employeeIdInput = tk.Text(employeeIdFrame, height=1, width=15)
employeeIdInput.pack(side=tk.LEFT)
employeeIdFrame.pack()

firstNameFrame = tk.Frame(createNewEmployee)
firstNameLabel = tk.Label(firstNameFrame, text="New Employee First Name: ")
firstNameLabel.pack(side=tk.LEFT)
firstNameInput = tk.Text(firstNameFrame, height=1, width=15)
firstNameInput.pack(side=tk.LEFT)
firstNameFrame.pack()

lastNameFrame = tk.Frame(createNewEmployee)
lastNameLabel = tk.Label(lastNameFrame, text="New Employee Last Name: ")
lastNameLabel.pack(side=tk.LEFT)
lastNameInput = tk.Text(lastNameFrame, height=1, width=15)
lastNameInput.pack(side=tk.LEFT)
lastNameFrame.pack()

passwordFrame = tk.Frame(createNewEmployee)
passwordLabel = tk.Label(passwordFrame, text="New Employee Password: ")
passwordLabel.pack(side=tk.LEFT)
passwordInput = tk.Text(passwordFrame, height=1, width=15)
passwordInput.pack(side=tk.LEFT)
passwordFrame.pack()

isAdmin = tk.BooleanVar()
isAdminFrame = tk.Frame(createNewEmployee)
isAdminCheck = tk.Checkbutton(isAdminFrame, text="Administrator", variable=isAdmin, onvalue=1, offvalue=0)
isAdminCheck.pack()
isAdminFrame.pack()

createButton = tk.Button(createNewEmployee, text="Create",
                         command=lambda:
                         createEmployee(employeeIdInput.get(1.0, "end-1c"),
                                        firstNameInput.get(1.0, "end-1c"),
                                        lastNameInput.get(1.0, "end-1c"),
                                        passwordInput.get(1.0, "end-1c"),
                                        isAdmin.get()))
createButton.pack(side=tk.RIGHT)
createButton = tk.Button(createNewEmployee, text="Back", command=back)
createButton.pack(side=tk.RIGHT)

createNewEmployee.mainloop()
