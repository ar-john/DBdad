import tkinter as tk

adminSearch = tk.Tk()
adminSearch.title("Admin Search")
adminSearch.geometry("250x150+50+50")

partNumSearch = tk.Frame(adminSearch)

partNumLabel = tk.Label(partNumSearch, text="Part Number: ")
partNumLabel.pack(side=tk.LEFT)
partNumInput = tk.Text(partNumSearch, height=1, width=15)
partNumInput.pack(side=tk.LEFT)

partNumSearch.pack()

chooseLabel = tk.Label(adminSearch, text="---or choose at least 1---")
chooseLabel.pack()

categories = ["Engine", "Lights", "Brakes", "Transmissions", "Windshield Wipers"]
descriptions=["Brake Pads", "Headlights", "Brake Lights", "Coilovers"]

selectCategory = tk.Frame(adminSearch)
selectCategoryLabel = tk.Label(selectCategory, text="Select Category: ")
selectCategoryLabel.pack(side=tk.LEFT)

category = tk.StringVar(selectCategory)
category.set(None)

categoryMenu = tk.OptionMenu(selectCategory, category, *categories)
categoryMenu.pack(side=tk.LEFT)

selectCategory.pack()

selectDescription = tk.Frame(adminSearch)
selectDescriptionLabel = tk.Label(selectDescription, text="Select Description: ")
selectDescriptionLabel.pack(side=tk.LEFT)

description = tk.StringVar(selectDescription)
description.set(None)

descriptionMenu = tk.OptionMenu(selectDescription, description, *descriptions)
descriptionMenu.pack(side=tk.LEFT)

selectDescription.pack()


def getProps():
    props = []
    if partNumInput.get(1.0, "end-1c") != None:
        props.append(partNumInput.get(1.0, "end-1c"))
    if category.get() != None:
        props.append(category.get())
    if description.get() != None:
        props.append(description.get())
    print(props)


def clearProps():
    category.set(None)
    description.set(None)

buttonFrame = tk.Frame(adminSearch)

searchButton = tk.Button(adminSearch, text="Search", command=getProps)
searchButton.pack(side=tk.RIGHT)

clearButton = tk.Button(adminSearch, text="Clear", command=clearProps)
clearButton.pack(side=tk.RIGHT)

buttonFrame.pack(side=tk.BOTTOM)

adminSearch.mainloop()
