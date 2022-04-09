import tkinter as tk

employeeAdministration = tk.Tk()
employeeAdministration.title("Employee Administration")
employeeAdministration.geometry('350x200+50+50')

def updateExisting():
    #launch employee search window
    return

def createNew():
    #launch create new employee window
    return

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

employeeAdministration.mainloop()