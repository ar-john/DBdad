import tkinter as tk
import connector


def adminPart(num, category, desc, Pprice, QTY, date):
    part = []

    def __init__(self):
        mydb = connector.DB()
        result = mydb.returnPart(num)

        for x in result:
            part.append(str(x))
        
        print(part)
        return part



    adminUpdatePage = tk.Tk()
    adminUpdatePage.title("Admin Part Update")
    adminUpdatePage.geometry('350x200+50+50')
    
    def getPart():
        mydb = connector.DB()
        # sql = ('select * from PART where PART_NUM= \'' + partNum + '\' ;')
        # mydb.cursor.execute(sql)
        # result = mydb.cursor.fetchall()
        # print(result)
        # for x in result:
        #     part.append(x)

        # print(part)
        # return part    
        # mydb.exit()
        mydb.updatePart(editStockInput.get(), editPriceInput.get(), num)


    partNum = num
    # partDescription = part[1]
    # partPrice = part[3]
    # qoh = part[4]

    descriptionFrame = tk.Frame(adminUpdatePage)
    partNumLabel = tk.Label(descriptionFrame, text="Part Number: "+ partNum)
    partNumLabel.pack()
    partNameLabel = tk.Label(descriptionFrame, text="Part Description: " + desc)
    partNameLabel.pack()
    qohLabel = tk.Label(descriptionFrame, text="Current Quantity: " + str(QTY))
    qohLabel.pack()
    partPriceLabel = tk.Label(descriptionFrame, text="Current Price: " + str(Pprice))
    partPriceLabel.pack()
    descriptionFrame.pack()

    editStockFrame = tk.Frame(adminUpdatePage)
    editStockLabel = tk.Label(editStockFrame, text="Update Stock: ")
    editStockLabel.pack(side=tk.LEFT)
    editStockInput = tk.Entry(editStockFrame, width=15)
    editStockInput.pack(side=tk.LEFT)
    editStockFrame.pack()

    editPriceFrame = tk.Frame(adminUpdatePage)
    editPriceLabel = tk.Label(editPriceFrame, text="Update Price: ")
    editPriceLabel.pack(side=tk.LEFT)
    editPriceInput = tk.Entry(editPriceFrame, width=15)
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

    cartButton = tk.Button(adminUpdatePage, text="Update", command=getPart)
    cartButton.pack(side=tk.RIGHT)

    backButton = tk.Button(adminUpdatePage, text="Cancel", command=back)
    backButton.pack(side=tk.RIGHT)

    buttonFrame.pack(side=tk.BOTTOM)

    getPart()


    adminUpdatePage.mainloop()

# adminPart('00001')