import tkinter as tk

adminConsole = tk.Tk()
adminConsole.title("Admin Console")
adminConsole.geometry('350x100+50+50')

def updateEmployee():
    #launch employee update screen
    return

def updatePart():
    #launch AdminSearch screen
    return

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