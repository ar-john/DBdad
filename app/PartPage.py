import sys
import tkinter as tk
from PIL import ImageTk, Image
from connector import DB
import PartFinder
import InvoiceGenerator
import EmployeeConsole

def partpageGui(partnum, invoiceNumber = None):
    db = DB()
    partPage = tk.Tk()
    partPage.title("Part Description")
    partPage.geometry('600x200+50+50')

    partProps = db.getPart(partnum)

    partPicture = Image.open("img/" + str(partProps[1])+'.jpg')
    partPicture = partPicture.resize((100, 100))
    partPicture = ImageTk.PhotoImage(partPicture)
    pictureLabel = tk.Label(partPage, image=partPicture)
    pictureLabel.pack(side=tk.LEFT)

    descriptionFrame = tk.Frame(partPage)
    partNumLabel = tk.Label(descriptionFrame, text="Part Number: "+ str(partProps[0]))
    partNumLabel.pack()
    partNameLabel = tk.Label(descriptionFrame, text="Part Description: " + str(partProps[2]))
    partNameLabel.pack()
    partPriceLabel = tk.Label(descriptionFrame, text="Price: " + str(partProps[3]))
    partPriceLabel.pack()
    qohLabel = tk.Label(descriptionFrame, text="Quantity: " + str(partProps[4]))
    qohLabel.pack()
    descriptionFrame.pack(side=tk.LEFT)

    def addToInvoice(part, qty):
        invoice = InvoiceGenerator.InvoiceGenerator()
        invoice.addPartToInvoice(invoiceNumber, part, qty)
        invoice.createInvoiceGraphics(invoiceNumber)
        partPage.destroy()
        window = tk.Toplevel(EmployeeConsole.EConsole())
        window.transient(partPage)
        return

    def back():
        partPage.destroy()
        window = tk.Toplevel(PartFinder.partWin(invoiceNumber))
        window.transient(partPage)
        return

    buttonFrame = tk.Frame(partPage)

    cartButton = tk.Button(buttonFrame, text="Add To Invoice " + invoiceNumber, command=lambda: addToInvoice(partProps[0], 1))
    cartButton.pack(side=tk.LEFT)

    backButton = tk.Button(buttonFrame, text="Back", command=back)
    backButton.pack(side = tk.LEFT)

    buttonFrame.pack(side=tk.BOTTOM)
    def on_closing():
        sys.exit()

    partPage.protocol("WM_DELETE_WINDOW", on_closing)

    partPage.mainloop()

#partpageGui('00001')