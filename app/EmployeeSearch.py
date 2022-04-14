import tkinter as tk
import connector
import UpdateExistingEmployee
import sys
import EmployeeAdministration

def searchEmp():
    


    searchEmployee = tk.Tk()
    searchEmployee.title("Search For Employee")
    searchEmployee.geometry('350x200+50+50')

    def search():
        mydb = connector.DB()
        # searchParams = []
        # searchParams.append(firstName)
        # searchParams.append(lastName)
        # print(searchParams)
        # return searchParams
        if mydb.searchEmpDB(firstNameInput.get(),lastNameInput.get()) == True:
            
            window = tk.Toplevel(UpdateExistingEmployee.UpdateExistingScreen(firstNameInput.get(),lastNameInput.get()))
            window.transient(window)
        else:
            print('Incorrect input')



    firstNameFrame = tk.Frame(searchEmployee)
    firstNameLabel = tk.Label(firstNameFrame, text="Employee First Name: ")
    firstNameLabel.pack(side=tk.LEFT)
    firstNameInput = tk.Entry(firstNameFrame, width=15)
    firstNameInput.pack(side=tk.LEFT)
    firstNameFrame.pack()

    lastNameFrame = tk.Frame(searchEmployee)
    lastNameLabel = tk.Label(lastNameFrame, text="Employee Last Name: ")
    lastNameLabel.pack(side=tk.LEFT)
    lastNameInput = tk.Entry(lastNameFrame, width=15)
    lastNameInput.pack(side=tk.LEFT)
    lastNameFrame.pack()

    searchButton = tk.Button(searchEmployee, text="Update", command=search)
    searchButton.pack(side=tk.RIGHT)
    # searchButton = tk.Button(searchEmployee, text="Back", command=back)
    # searchButton.pack(side=tk.RIGHT)

    buttonFrame = tk.Frame(searchEmployee)
    # createNewButton = tk.Button(createNewFrame, text="Create", command=createNew)

    def back():
        searchEmployee.destroy()
        window = tk.Toplevel(EmployeeAdministration.empAdmin())
        window.transient(searchEmployee)

    backButton = tk.Button(buttonFrame, text="Back", command=back)
    backButton.pack(side = tk.RIGHT)
    buttonFrame.pack()


    def on_closing():
        sys.exit()

    searchEmployee.protocol("WM_DELETE_WINDOW", on_closing)  

    searchEmployee.mainloop()

# searchEmp()