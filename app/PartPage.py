import tkinter as tk
from PIL import ImageTk, Image

def partpageGui():

    partPage = tk.Tk()
    partPage.title("Part Description")
    partPage.geometry('350x200+50+50')

    partPicture = Image.open('app/ej engine.jpg')
    partPicture = partPicture.resize((100, 100))
    partPicture = ImageTk.PhotoImage(partPicture)
    pictureLabel = tk.Label(partPage, image=partPicture)
    pictureLabel.pack(side=tk.LEFT)

    partNum = 42069
    partPrice = 15.99
    qoh = 10
    availableBy = "4/8/2022"

    descriptionFrame = tk.Frame(partPage)
    partNumLabel = tk.Label(descriptionFrame, text="Part Number: "+ str(partNum))
    partNumLabel.pack()
    partPriceLabel = tk.Label(descriptionFrame, text="Price: " + str(partPrice))
    partPriceLabel.pack()
    qohLabel = tk.Label(descriptionFrame, text="Quantity: " + str(qoh))
    qohLabel.pack()
    availableByLabel = tk.Label(descriptionFrame, text="Available by: " + availableBy)
    availableByLabel.pack()
    descriptionFrame.pack(side=tk.LEFT)

    def addToInvoice():
        part = []
        part.append(partNum)
        part.append(partPrice)
        part.append(qoh)
        part.append(availableBy)
        return part

    def back():
        return None

    buttonFrame = tk.Frame(partPage)

    cartButton = tk.Button(buttonFrame, text="Add To Cart", command=addToInvoice)
    cartButton.pack(side=tk.RIGHT)

    backButton = tk.Button(buttonFrame, text="Back", command=back)
    backButton.pack(side=tk.RIGHT)

    buttonFrame.pack(side=tk.BOTTOM)


    partPage.mainloop()
