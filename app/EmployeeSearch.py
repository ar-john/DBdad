import tkinter as tk

searchEmployee = tk.Tk()
searchEmployee.title("Search For Employee")
searchEmployee.geometry('350x200+50+50')

def search(firstName, lastName):
    searchParams = []
    searchParams.append(firstName)
    searchParams.append(lastName)
    print(searchParams)
    return searchParams

def back():
    return

firstNameFrame = tk.Frame(searchEmployee)
firstNameLabel = tk.Label(firstNameFrame, text="Employee First Name: ")
firstNameLabel.pack(side=tk.LEFT)
firstNameInput = tk.Text(firstNameFrame, height=1, width=15)
firstNameInput.pack(side=tk.LEFT)
firstNameFrame.pack()

lastNameFrame = tk.Frame(searchEmployee)
lastNameLabel = tk.Label(lastNameFrame, text="Employee Last Name: ")
lastNameLabel.pack(side=tk.LEFT)
lastNameInput = tk.Text(lastNameFrame, height=1, width=15)
lastNameInput.pack(side=tk.LEFT)
lastNameFrame.pack()

searchButton = tk.Button(searchEmployee, text="Update",
                         command=lambda:
                         search(firstNameInput.get(1.0, "end-1c"),
                                        lastNameInput.get(1.0, "end-1c")))
searchButton.pack(side=tk.RIGHT)
searchButton = tk.Button(searchEmployee, text="Back", command=back)
searchButton.pack(side=tk.RIGHT)

searchEmployee.mainloop()