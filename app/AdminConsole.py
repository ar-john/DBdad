
import tkinter as tk
import AdminPartUpdate
import EmployeeAdministration
import AdminSearch
import sys





def AdminCon():

    

    def updateEmployee():
        #launch employee update screen
        adminConsole.destroy()
        window = tk.Toplevel(EmployeeAdministration.empAdmin())
        window.transient(window)
        
        
        
        


    #method to take us to the Adminpartupdate page
    def updatePart():
        #launch AdminSearch screen
        adminConsole.destroy()
        window = tk.Toplevel(AdminSearch.adSearch())
        window.transient(window)
        

        

    

    adminConsole = tk.Tk()
    adminConsole.title("Admin Console")
    adminConsole.geometry('350x100+50+50')


    updateEmployeeFrame = tk.Frame(adminConsole)
    updateEmployeeLabel = tk.Label(updateEmployeeFrame, text="Update Employee: ")
    updateEmployeeLabel.pack(side=tk.LEFT)
    updateEmployeeButton = tk.Button(updateEmployeeFrame, text="Update", command=updateEmployee)
    updateEmployeeButton.pack(side=tk.LEFT)
    updateEmployeeFrame.pack()

    updatePartFrame = tk.Frame(adminConsole)
    updatePartLabel = tk.Label(updatePartFrame, text="Update Part: ")
    updatePartLabel.pack(side=tk.LEFT)
    updatePartButton = tk.Button(updatePartFrame, text="Update", command=updatePart)
    updatePartButton.pack(side=tk.LEFT)
    updatePartFrame.pack()

    

    def on_closing():
        sys.exit()

    adminConsole.protocol("WM_DELETE_WINDOW", on_closing)

    adminConsole.mainloop()

    # return adminConsole
# AdminCon()