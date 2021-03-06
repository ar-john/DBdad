#!/usr/bin/python
import sys
import tkinter as tk
from connector import DB
import PartPage
import EmployeeConsole

def partWin(invoiceNumber = None, carid = None):
    #creates a db object
    db = DB()
    #create part finder window
    partFinder = tk.Tk()
    partFinder.title("Part Finder")
    partFinder.geometry('400x250+50+50')
    make = tk.StringVar(partFinder)
    model = tk.StringVar(partFinder)
    category = tk.StringVar(partFinder)
    description = tk.StringVar(partFinder)

    years = db.getCarYears()

    def yearCallback(*args):
        selectMake = tk.Frame(partFinder)
        selectMakeLabel = tk.Label(selectMake, text="Select Make: ")
        selectMakeLabel.pack(side=tk.LEFT)
        make.set(None)
        make.trace("w", makeCallback)
        makes = db.getMakesByYear(year.get())
        makeMenu = tk.OptionMenu(selectMake, make, *makes)
        makeMenu.pack(side=tk.LEFT)
        selectMake.pack()

    def makeCallback(*args):
        selectModel = tk.Frame(partFinder)
        selectModelLabel = tk.Label(selectModel, text="Select Model: ")
        selectModelLabel.pack(side=tk.LEFT)
        model.set(None)
        model.trace("w", modelCallback)
        models = db.getModelsByMake(make.get())
        modelMenu = tk.OptionMenu(selectModel, model, *models)
        modelMenu.pack(side=tk.LEFT)
        selectModel.pack()

    def modelCallback(*args):
        selectCategory = tk.Frame(partFinder)
        selectCategoryLabel = tk.Label(selectCategory, text="Select Category: ")
        selectCategoryLabel.pack(side=tk.LEFT)
        category.set(None)
        category.trace("w", categoryCallBack)
        compatibility = (db.getCompatibility(year.get(), make.get(), model.get())[0])
        categories = db.getPartCategories(compatibility)
        categoryMenu = tk.OptionMenu(selectCategory, category, *categories)
        categoryMenu.pack(side=tk.LEFT)
        selectCategory.pack()

    def categoryCallBack(*args):
        selectDescription = tk.Frame(partFinder)
        selectDescriptionLabel = tk.Label(selectDescription, text="Select Description: ")
        selectDescriptionLabel.pack(side=tk.LEFT)
        description.set(None)
        compatibility = (db.getCompatibility(year.get(), make.get(), model.get())[0])
        descriptions = db.getPartDescriptions(category.get(), compatibility)
        descriptionMenu = tk.OptionMenu(selectDescription, description, *descriptions)
        descriptionMenu.pack(side=tk.LEFT)
        selectDescription.pack()


    #create select year label and menu
    selectYear = tk.Frame(partFinder)
    selectYearLabel = tk.Label(selectYear, text="Select Vehicle Year: ")
    selectYearLabel.pack(side=tk.LEFT)

    year = tk.StringVar(selectYear)
    year.set(None)
    year.trace("w", yearCallback)

    yearMenu = tk.OptionMenu(selectYear, year, *years)
    yearMenu.pack(side=tk.LEFT)

    selectYear.pack()

    if carid:
        car = db.getCar(carid)
        year.set(car[1])
        make.set(car[2])
        model.set(car[3])

    # def getProps():
    #     props = []
    #     props.append(year.get())
    #     props.append(make.get())
    #     props.append(model.get())
    #     props.append(category.get())
    #     props.append(description.get())
    #     part = db.searchPart(props)
    #     partFinder.destroy()
    #     window = tk.Toplevel(PartPage.partpageGui(part, invoiceNumber))
    #     window.transient(partFinder)
    def getProps():
        props = []
        props.append(year.get())
        props.append(make.get())
        props.append(model.get())
        props.append(category.get())
        props.append(description.get())
        parts = db.searchPart(props)
        print(parts)
        for part in parts:
            partFinder.destroy()
            window = tk.Toplevel(PartPage.partpageGui(part, invoiceNumber))
            window.transient(partFinder)

    def back():
        partFinder.destroy()
        window = tk.Toplevel(EmployeeConsole.EConsole())
        window.transient(partFinder)

    buttonGroup = tk.Frame(partFinder)

    searchButton = tk.Button(partFinder, text="Search", command=getProps)
    searchButton.pack(side=tk.RIGHT)

    clearButton = tk.Button(partFinder, text="Back", command=back)
    clearButton.pack(side=tk.RIGHT)

    buttonGroup.pack(side=tk.BOTTOM)

    def on_closing():
        sys.exit()

    partFinder.protocol("WM_DELETE_WINDOW", on_closing)

    partFinder.mainloop()

#partWin()