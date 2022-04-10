import tkinter as tk

def newEmp():
    createNewEmployee = tk.Tk()
    createNewEmployee.title("Create New Employee")
    createNewEmployee.geometry('350x200+50+50')

    def createEmployee(firstName, lastName, admin):
        lastEmployeeId = 16
        newEmployee =[]
        newEmployee.append(lastEmployeeId + 1)
        newEmployee.append(firstName)
        newEmployee.append(lastName)
        newEmployee.append(admin)
        newEmployee.append("Password")
        print(newEmployee)
        return newEmployee

    def back():
        return

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

    isAdmin = tk.BooleanVar()
    isAdminFrame = tk.Frame(createNewEmployee)
    isAdminCheck = tk.Checkbutton(isAdminFrame, text="Administrator", variable=isAdmin, onvalue=1, offvalue=0)
    isAdminCheck.pack()
    isAdminFrame.pack()

    createButton = tk.Button(createNewEmployee, text="Create",
                            command=lambda:
                            createEmployee(firstNameInput.get(1.0, "end-1c"),
                                            lastNameInput.get(1.0, "end-1c"),
                                            isAdmin.get()))
    createButton.pack(side=tk.RIGHT)
    createButton = tk.Button(createNewEmployee, text="Back", command=back)
    createButton.pack(side=tk.RIGHT)

    createNewEmployee.mainloop()