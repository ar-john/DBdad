import tkinter as tk
import PartFinder
#Piston icons created by wanicon - Flaticon

def empConsole():
    employeeConsole = tk.Tk()
    employeeConsole.title("Employee Console")
    employeeConsole.geometry('350x100+50+50')
    
    def createCustomer():
        return
    
    def createInvoice(custPhone):
        print(custPhone)
        return custPhone
    
    def openPartFinder():
        """employeeConsole.destroy()
        window = tk.Toplevel(PartFinder.partWin())
        window.transient(window)"""
        return

    createCustomerFrame = tk.Frame(employeeConsole)
    createCustomerLabel = tk.Label(createCustomerFrame, text="Customer: ")
    createCustomerLabel.pack(side=tk.LEFT)
    createCustomerButton = tk.Button(createCustomerFrame, text="Create", command=createCustomer)
    createCustomerButton.pack(side=tk.LEFT)
    createCustomerFrame.pack()

    createInvoiceFrame = tk.Frame(employeeConsole)
    createInvoiceLabel = tk.Label(createInvoiceFrame, text="Create Invoice: ")
    createInvoiceLabel.pack(side=tk.LEFT)
    createInvoiceButton = tk.Button(createInvoiceFrame, text="Create", command=createInvoice)
    createInvoiceButton.pack(side=tk.LEFT)
    createInvoiceFrame.pack()

    partFinderFrame = tk.Frame(employeeConsole)
    partFinderLabel = tk.Label(partFinderFrame, text="Launch Part Finder: ")
    partFinderLabel.pack(side=tk.LEFT)
    partFinderButton = tk.Button(partFinderFrame, text="Launch", command=openPartFinder)
    partFinderButton.pack(side=tk.LEFT)
    partFinderFrame.pack()

    employeeConsole.mainloop()

# empConsole()