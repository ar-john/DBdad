import tkinter as tk
import sys

def CreateCustomerScreen():
    createCustomer = tk.Tk()
    createCustomer.title("Create Customer")
    createCustomer.geometry('350x200+50+50')

    def customerCreate(phone, car):
        customerProps = []
        customerProps.append(phone)
        customerProps.append(car)
        print(customerProps)
        return customerProps

   

    customerIdFrame = tk.Frame(createCustomer)
    customerIdLabel = tk.Label(customerIdFrame, text="New Customer ID: ")
    customerIdLabel.pack(side=tk.LEFT)
    customerIdInput = tk.Entry(customerIdFrame)
    customerIdInput.pack(side=tk.LEFT)
    customerIdFrame.pack()

    carIdFrame = tk.Frame(createCustomer)
    carIdLabel = tk.Label(carIdFrame, text="Customer CarId: ")
    carIdLabel.pack(side=tk.LEFT)
    carIdInput = tk.Entry(carIdFrame)
    carIdInput.pack(side=tk.LEFT)
    carIdFrame.pack()

    createButton = tk.Button(createCustomer, text="Create",
                             command=lambda:
                             customerCreate(customerIdInput.get(),
                                            carIdInput.get()))
    createButton.pack(side=tk.RIGHT)
    createButton = tk.Button(createCustomer, text="Back", command=back)
    createButton.pack(side=tk.RIGHT)

    # def back():
    #     adminSearch.destroy()
    #     window = tk.Toplevel(AdminConsole.AdminCon())
    #     window.transient(adminSearch)

    def on_closing():
        sys.exit()

    createCustomer.protocol("WM_DELETE_WINDOW", on_closing)

    createCustomer.mainloop()

#CreateCustomerScreen()