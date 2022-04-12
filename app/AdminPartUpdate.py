import tkinter as tk
import connector


def adminPart(num):
    adminUpdatePage = tk.Tk()
    adminUpdatePage.title("Admin Part Update")
    adminUpdatePage.geometry('350x200+50+50')
    part = []
    def getPart():
        mydb = connector.DB()
        sql = ('select * from PART where PART_NUM= \'' + partNum + '\' ;')
        mydb.cursor.execute(sql)
        result = mydb.cursor.fetchall()
        print(result)
        for x in result:
            part.append(x)

        print(part)
        return part    
        mydb.exit()


    partNum = num
    partDescription = part[1]
    partPrice = part[3]
    qoh = part[4]

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

    getPart()


    adminUpdatePage.mainloop()