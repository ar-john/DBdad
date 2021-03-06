import tkinter as tk


import CreateNewEmployee
import EmployeeSearch
import sys
import AdminConsole
# from app.AdminConsole import AdminCon



def empAdmin():

    employeeAdministration = tk.Tk()
    employeeAdministration.title("Employee Administration")
    employeeAdministration.geometry('350x200+50+50')

    def updateExisting():
        #launch employee search window
        
        employeeAdministration.destroy()
        window = tk.Toplevel(EmployeeSearch.searchEmp())
        window.transient(window)

       

    def createNew():
        #launch create new employee window
        employeeAdministration.destroy()
        window = tk.Toplevel(CreateNewEmployee.newEmp())
        window.transient(window)


    updateExistingFrame = tk.Frame(employeeAdministration)
    updateExistingLabel = tk.Label(updateExistingFrame, text="Update Existing Employee: ")
    updateExistingLabel.pack(side=tk.LEFT)
    updateExistingButton = tk.Button(updateExistingFrame, text="Update", command=updateExisting)
    updateExistingButton.pack(side=tk.LEFT)
    updateExistingFrame.pack()

    createNewFrame = tk.Frame(employeeAdministration)
    createNewLabel = tk.Label(createNewFrame, text="Create New Employee: ")
    createNewLabel.pack(side=tk.LEFT)
    createNewButton = tk.Button(createNewFrame, text="Create", command=createNew)
    createNewButton.pack(side=tk.LEFT)
    createNewFrame.pack()

    buttonFrame = tk.Frame(employeeAdministration)
    # createNewButton = tk.Button(createNewFrame, text="Create", command=createNew)

    def back():
        employeeAdministration.destroy()
        window = tk.Toplevel(AdminConsole.AdminCon())
        window.transient(employeeAdministration)

    backButton = tk.Button(buttonFrame, text="Back", command=back)
    backButton.pack(side = tk.RIGHT)
    buttonFrame.pack()

    def on_closing():
        sys.exit()

    employeeAdministration.protocol("WM_DELETE_WINDOW", on_closing)

    employeeAdministration.mainloop()
# empAdmin()