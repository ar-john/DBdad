
import tkinter as tk
import AdminPartUpdate


    
# import UpdateExistingEmployee
# import AdminPartUpdate

def updateEmployee():
    #launch employee update screen
    
    return


def AdminCon():
    def updatePart():
        #launch AdminSearch screen
        adminConsole.destroy()
        window = tk.Toplevel(AdminPartUpdate.adminPart())
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

    adminConsole.mainloop()