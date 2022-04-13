import tkinter as tk
import PartFinder
import CreateCustomer
import InvoiceGenerator

class EConsole:
    employeeConsole = tk.Tk()
    employeeConsole.title("Employee Console")
    employeeConsole.geometry('350x100+50+50')
#  <<<<<<< employee-features
    invoiceNumber = ""

    def empConsole(self):

        def createCustomer():
            return

        def createInvoice():
            top = tk.Toplevel(self.employeeConsole)
            top.geometry("350x100+60+60")
            top.title("Create Invoice")

            def create(custid, empid):
                invoice = InvoiceGenerator.InvoiceGenerator()
                invoice.createInvoice(custid, empid)
                self.invoiceNumber = invoice.getInvoiceNumber()
                print("invoice " + self.invoiceNumber + " created")
                top.destroy()

            customerIdFrame = tk.Frame(top)
            customerIdLabel = tk.Label(customerIdFrame, text="Customer ID: ")
            customerIdLabel.pack(side=tk.LEFT)
            customerIdInput = tk.Entry(customerIdFrame)
            customerIdInput.pack(side=tk.LEFT)
            customerIdFrame.pack()
            employeeIdFrame = tk.Frame(top)
            employeeIdLabel = tk.Label(employeeIdFrame, text="Employee ID: ")
            employeeIdLabel.pack(side=tk.LEFT)
            employeeIdInput = tk.Entry(employeeIdFrame)
            employeeIdInput.pack(side=tk.LEFT)
            employeeIdFrame.pack()
            createButton = tk.Button(top, text="Create",
                                     command=lambda:
                                     create(customerIdInput.get(),
                                            employeeIdInput.get()))
            createButton.pack(side=tk.RIGHT)



        def openPartFinder():
            self.employeeConsole.destroy()
            top = tk.Toplevel(PartFinder.partWin(self.invoiceNumber))
            top.transient(self.employeeConsole)


        createCustomerFrame = tk.Frame(self.employeeConsole)
        createCustomerLabel = tk.Label(createCustomerFrame, text="Customer: ")
        createCustomerLabel.pack(side=tk.LEFT)
        createCustomerButton = tk.Button(createCustomerFrame, text="Create", command=createCustomer)
        createCustomerButton.pack(side=tk.LEFT)
        createCustomerFrame.pack()

        createInvoiceFrame = tk.Frame(self.employeeConsole)
        createInvoiceLabel = tk.Label(createInvoiceFrame, text="Create Invoice: ")
        createInvoiceLabel.pack(side=tk.LEFT)
        createInvoiceButton = tk.Button(createInvoiceFrame, text="Create", command=createInvoice)
        createInvoiceButton.pack(side=tk.LEFT)
        createInvoiceFrame.pack()

        partFinderFrame = tk.Frame(self.employeeConsole)
        partFinderLabel = tk.Label(partFinderFrame, text="Launch Part Finder: ")
        partFinderLabel.pack(side=tk.LEFT)
        partFinderButton = tk.Button(partFinderFrame, text="Launch", command=openPartFinder)
        partFinderButton.pack(side=tk.LEFT)
        partFinderFrame.pack()

        self.employeeConsole.mainloop()

# #empConsole()
# =======
    
#     def createCustomer():
#         return
    
#     def createInvoice(custPhone):
#         print(custPhone)
#         return custPhone
    
#     def openPartFinder():
#         """employeeConsole.destroy()
#         window = tk.Toplevel(PartFinder.partWin())
#         window.transient(window)"""
#         return

#     createCustomerFrame = tk.Frame(employeeConsole)
#     createCustomerLabel = tk.Label(createCustomerFrame, text="Customer: ")
#     createCustomerLabel.pack(side=tk.LEFT)
#     createCustomerButton = tk.Button(createCustomerFrame, text="Create", command=createCustomer)
#     createCustomerButton.pack(side=tk.LEFT)
#     createCustomerFrame.pack()

#     createInvoiceFrame = tk.Frame(employeeConsole)
#     createInvoiceLabel = tk.Label(createInvoiceFrame, text="Create Invoice: ")
#     createInvoiceLabel.pack(side=tk.LEFT)
#     createInvoiceButton = tk.Button(createInvoiceFrame, text="Create", command=createInvoice)
#     createInvoiceButton.pack(side=tk.LEFT)
#     createInvoiceFrame.pack()

#     partFinderFrame = tk.Frame(employeeConsole)
#     partFinderLabel = tk.Label(partFinderFrame, text="Launch Part Finder: ")
#     partFinderLabel.pack(side=tk.LEFT)
#     partFinderButton = tk.Button(partFinderFrame, text="Launch", command=openPartFinder)
#     partFinderButton.pack(side=tk.LEFT)
#     partFinderFrame.pack()

#     employeeConsole.mainloop()

# # empConsole()
#  >>>>>>> master
