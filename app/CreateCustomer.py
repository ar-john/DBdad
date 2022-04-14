import tkinter as tk
from venv import create
from connector import DB
import sys
import EmployeeConsole

def CreateCustomerScreen():
    createCustomer = tk.Tk()
    createCustomer.title("Create Customer")
    createCustomer.geometry('350x200+50+50')
    make = tk.StringVar(createCustomer)
    model = tk.StringVar(createCustomer)

    db = DB()

    years = db.getCarYears()

    def customerCreate():
        car = db.getCarByYMM(year.get(), make.get(), model.get())
        db.createCustomer(customerFnameInput.get(), customerLnameInput.get(), car)
        createCustomer.destroy()
        top = tk.Toplevel(EmployeeConsole.EConsole())
        top.transient(customerCreate)

    def back():
        createCustomer.destroy()
        top = tk.Toplevel(EmployeeConsole.EConsole())
        top.transient(customerCreate)

    customerFnameFrame = tk.Frame(createCustomer)
    customerFnameLabel = tk.Label(customerFnameFrame, text="New Customer First Name: ")
    customerFnameLabel.pack(side=tk.LEFT)
    customerFnameInput = tk.Entry(customerFnameFrame)
    customerFnameInput.pack(side=tk.LEFT)
    customerFnameFrame.pack()

    customerLnameFrame = tk.Frame(createCustomer)
    customerLnameLabel = tk.Label(customerLnameFrame, text="New Customer Last Name: ")
    customerLnameLabel.pack(side=tk.LEFT)
    customerLnameInput = tk.Entry(customerLnameFrame)
    customerLnameInput.pack(side=tk.LEFT)
    customerLnameFrame.pack()

    def yearCallback(*args):
        selectMake = tk.Frame(createCustomer)
        selectMakeLabel = tk.Label(selectMake, text="Select Make: ")
        selectMakeLabel.pack(side=tk.LEFT)
        make.set(None)
        make.trace("w", makeCallback)
        makes = db.getMakesByYear(year.get())
        makeMenu = tk.OptionMenu(selectMake, make, *makes)
        makeMenu.pack(side=tk.LEFT)
        selectMake.pack()

    def makeCallback(*args):
        selectModel = tk.Frame(createCustomer)
        selectModelLabel = tk.Label(selectModel, text="Select Model: ")
        selectModelLabel.pack(side=tk.LEFT)
        model.set(None)
        model.trace("w", modelCallback)
        models = db.getModelsByMake(make.get())
        modelMenu = tk.OptionMenu(selectModel, model, *models)
        modelMenu.pack(side=tk.LEFT)
        selectModel.pack()

    def modelCallback(*args):
        return

    selectYear = tk.Frame(createCustomer)
    selectYearLabel = tk.Label(selectYear, text="Select Vehicle Year: ")
    selectYearLabel.pack(side=tk.LEFT)

    year = tk.StringVar(selectYear)
    year.set(None)
    year.trace("w", yearCallback)

    yearMenu = tk.OptionMenu(selectYear, year, *years)
    yearMenu.pack(side=tk.LEFT)

    selectYear.pack()

        

    createButton = tk.Button(createCustomer, text="Create",
                             command=customerCreate)
    createButton.pack(side=tk.RIGHT)
    createButton = tk.Button(createCustomer, text="Back", command=back)
    createButton.pack(side=tk.RIGHT)

    def on_closing():
            sys.exit()

    createCustomer.protocol("WM_DELETE_WINDOW", on_closing)


    createCustomer.mainloop()

#CreateCustomerScreen()