import tkinter as tk

def UpdateExistingScreen():
    updateExistingEmployee = tk.Tk()
    updateExistingEmployee.title("Update Existing Employee")
    updateExistingEmployee.geometry('350x200+50+50')

    def updateEmployee(admin, password):
        updateProps = []
        updateProps.append(admin)
        updateProps.append(password)
        print(updateProps)
        return updateProps

    def back():
        return

    passwordFrame = tk.Frame(updateExistingEmployee)
    passwordLabel = tk.Label(passwordFrame, text="Reset Employee Password: ")
    passwordLabel.pack(side=tk.LEFT)
    passwordInput = tk.Text(passwordFrame, height=1, width=15)
    passwordInput.pack(side=tk.LEFT)
    passwordFrame.pack()

    isAdmin = tk.BooleanVar()
    isAdminFrame = tk.Frame(updateExistingEmployee)
    isAdminCheck = tk.Checkbutton(isAdminFrame, text="Make Administrator?", variable=isAdmin, onvalue=1, offvalue=0)
    isAdminCheck.pack()
    isAdminFrame.pack()

    createButton = tk.Button(updateExistingEmployee, text="Update",
                             command=lambda:
                             updateEmployee(passwordInput.get(1.0, "end-1c"),
                                            isAdmin.get()))
    createButton.pack(side=tk.RIGHT)
    backButton = tk.Button(updateExistingEmployee, text="Back", command=back)
    backButton.pack(side=tk.RIGHT)

    updateExistingEmployee.mainloop()

#UpdateExistingScreen()