import tkinter as tk

adminUpdatePage = tk.Tk()
adminUpdatePage.title("Admin Part Update")
adminUpdatePage.geometry('350x200+50+50')

partNum = 42069
partDescription = "EJ engine for Subaru WRX"
partPrice = 15.99
qoh = 10

descriptionFrame = tk.Frame(adminUpdatePage)
partNumLabel = tk.Label(descriptionFrame, text="Part Number: "+ str(partNum))
partNumLabel.pack()
partNameLabel = tk.Label(descriptionFrame, text="Part Description: " + partDescription)
partNameLabel.pack()
qohLabel = tk.Label(descriptionFrame, text="Current Quantity: " + str(qoh))
qohLabel.pack()
partPriceLabel = tk.Label(descriptionFrame, text="Current Price: " + str(partPrice))
partPriceLabel.pack()
descriptionFrame.pack()

editStockFrame = tk.Frame(adminUpdatePage)
editStockLabel = tk.Label(editStockFrame, text="Update Stock: ")
editStockLabel.pack(side=tk.LEFT)
editStockInput = tk.Text(editStockFrame, height=1, width=15)
editStockInput.pack(side=tk.LEFT)
editStockFrame.pack()

editPriceFrame = tk.Frame(adminUpdatePage)
editPriceLabel = tk.Label(editPriceFrame, text="Update Price: ")
editPriceLabel.pack(side=tk.LEFT)
editPriceInput = tk.Text(editPriceFrame, height=1, width=15)
editPriceInput.pack(side=tk.LEFT)
editPriceFrame.pack()


def updatePart():
    partUpdate = []
    partUpdate.append(partNum)
    partUpdate.append(editStockInput.get(1.0, "end-1c"))
    partUpdate.append(editPriceInput.get(1.0, "end-1c"))
    print(partUpdate)
    return partUpdate

def back():
    return None

buttonFrame = tk.Frame(adminUpdatePage)

cartButton = tk.Button(adminUpdatePage, text="Update", command=updatePart)
cartButton.pack(side=tk.RIGHT)

backButton = tk.Button(adminUpdatePage, text="Cancel", command=back)
backButton.pack(side=tk.RIGHT)

buttonFrame.pack(side=tk.BOTTOM)


adminUpdatePage.mainloop()