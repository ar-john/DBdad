import tkinter as tk
import connector
import sys
import EmployeeSearch

def UpdateExistingScreen(firstN, lastN):
    updateExistingEmployee = tk.Tk()
    updateExistingEmployee.title("Update Existing Employee")
    updateExistingEmployee.geometry('350x200+50+50')

    def updateEmployee():
        mydb = connector.DB()
        updateProps = []
        updateProps.append(firstN)
        updateProps.append(lastN)
        print(updateProps)
        mydb.updateEmp(isAdmin.get(), passwordInput.get(), firstN, lastN)
    def back():
        updateExistingEmployee.destroy()
        window = tk.Toplevel(EmployeeSearch.searchEmp())
        window.transient(updateEmployee)    
        

    passwordFrame = tk.Frame(updateExistingEmployee)
    passwordLabel = tk.Label(passwordFrame, text="Reset Employee Password: ")
    passwordLabel.pack(side=tk.LEFT)
    passwordInput = tk.Entry(passwordFrame, width=15)
    passwordInput.pack(side=tk.LEFT)
    passwordFrame.pack()

    isAdmin = tk.BooleanVar()
    isAdminFrame = tk.Frame(updateExistingEmployee)
    isAdminCheck = tk.Checkbutton(isAdminFrame, text="Make Administrator?", variable=isAdmin, onvalue=1, offvalue=0)
    isAdminCheck.pack()
    isAdminFrame.pack()

    createButton = tk.Button(updateExistingEmployee, text="Update", command= updateEmployee)
    createButton.pack(side=tk.RIGHT)
    backButton = tk.Button(updateExistingEmployee, text="Back", command=back)
    backButton.pack(side=tk.RIGHT)

    # buttonFrame = tk.Frame(updateExistingEmployee)
    # createNewButton = tk.Button(createNewFrame, text="Create", command=createNew)

    

    # backButton = tk.Button(buttonFrame, text="Back", command=back)
    # backButton.pack(side = tk.RIGHT)
    # buttonFrame.pack()


    def on_closing():
        sys.exit()

    updateExistingEmployee.protocol("WM_DELETE_WINDOW", on_closing)

    updateExistingEmployee.mainloop()

# UpdateExistingScreen()