import sys
import tkinter as tk
import PartFinder
import CreateCustomer
import InvoiceGenerator
from connector import DB

class EConsole:

    employeeConsole = None

    invoiceNumber = ""
    db = DB()
    def __init__(self):
        self.employeeConsole = tk.Tk()
        self.employeeConsole.title("Employee Console")
        self.employeeConsole.geometry('350x100+50+50')
        self.invoiceNumber = ""
        createCustomerFrame = tk.Frame(self.employeeConsole)
        createCustomerLabel = tk.Label(createCustomerFrame, text="Customer: ")
        createCustomerLabel.pack(side=tk.LEFT)
        createCustomerButton = tk.Button(createCustomerFrame, text="Create", command=self.createCustomer)
        createCustomerButton.pack(side=tk.LEFT)
        createCustomerFrame.pack()

        createInvoiceFrame = tk.Frame(self.employeeConsole)
        createInvoiceLabel = tk.Label(createInvoiceFrame, text="Create Invoice: ")
        createInvoiceLabel.pack(side=tk.LEFT)
        createInvoiceButton = tk.Button(createInvoiceFrame, text="Create", command=self.createInvoice)
        createInvoiceButton.pack(side=tk.LEFT)
        createInvoiceFrame.pack()

        partFinderFrame = tk.Frame(self.employeeConsole)
        partFinderLabel = tk.Label(partFinderFrame, text="Launch Part Finder: ")
        partFinderLabel.pack(side=tk.LEFT)
        partFinderButton = tk.Button(partFinderFrame, text="Launch", command=self.openPartFinder)
        partFinderButton.pack(side=tk.LEFT)
        partFinderFrame.pack()

        def on_closing():
            sys.exit()

        self.employeeConsole.protocol("WM_DELETE_WINDOW", on_closing)

        self.employeeConsole.mainloop()

    def createCustomer(self):
        self.employeeConsole.destroy()
        top = tk.Toplevel(CreateCustomer.CreateCustomerScreen())
        top.transient(self.employeeConsole)

    def createInvoice(self):
        top = tk.Toplevel(self.employeeConsole)
        top.geometry("350x200+60+60")
        top.title("Create Invoice")

        def create(empid):
            invoice = InvoiceGenerator.InvoiceGenerator()
            invoice.createInvoice(self.db.getCustomerNumByName(customer.get()), empid)
            self.invoiceNumber = invoice.getInvoiceNumber()
            print("invoice " + self.invoiceNumber + " created")
            customerNumber = self.db.getCustomerNumByName(customer.get())
            customerCar = self.db.getCustomerCar(customerNumber[0])
            top.destroy()
            topTop = tk.Toplevel(self.employeeConsole)
            topTop.geometry("350x100+60+60")
            topTop.title("Invoice " + self.invoiceNumber + " Created")
            addPartButton = tk.Button(topTop, text="Add Part to Invoice", command = lambda: self.openPartFinder(customerCar[0]))
            addPartButton.pack()

        customer = tk.StringVar()
        selectCustomer = tk.Frame(top)
        selectCustomerLabel = tk.Label(selectCustomer, text="Select Customer: ")
        selectCustomerLabel.pack(side=tk.LEFT)
        customer.set(None)
        customers = self.db.getCustomers()
        customerMenu = tk.OptionMenu(selectCustomer, customer, *customers)
        customerMenu.pack(side=tk.LEFT)
        selectCustomer.pack()

        employeeIdFrame = tk.Frame(top)
        employeeIdLabel = tk.Label(employeeIdFrame, text="Employee ID: ")
        employeeIdLabel.pack(side=tk.LEFT)
        employeeIdInput = tk.Entry(employeeIdFrame)
        employeeIdInput.pack(side=tk.LEFT)
        employeeIdFrame.pack()
        createButton = tk.Button(top, text="Create",
                                    command=lambda:
                                    create(employeeIdInput.get()))
        createButton.pack(side=tk.RIGHT)



    def openPartFinder(self, car = None):
        self.employeeConsole.destroy()
        top = tk.Toplevel(PartFinder.partWin(self.invoiceNumber, car))
        top.transient(self.employeeConsole)

