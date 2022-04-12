#!/usr/bin/python
import tkinter as tk


from connector import DB

def partWin():
    #creates a db object
    db = DB()
    #create part finder window
    partFinder = tk.Tk()
    partFinder.title("Part Finder")
    partFinder.geometry('400x250+50+50')
    make = tk.StringVar(partFinder)
    model = tk.StringVar(partFinder)

    years = db.getCarYears()
    makes = []
    models = []

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
        models = db.getModelsByMake(make.get())
        modelMenu = tk.OptionMenu(selectModel, model, *models)
        modelMenu.pack(side=tk.LEFT)
        selectModel.pack()


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

    """
    makes = ["All Makes"]

    #create make label and menu in new frame
    selectMake = tk.Frame(partFinder)
    selectMakeLabel = tk.Label(selectMake, text="Select Make: ")
    selectMakeLabel.pack(side=tk.LEFT)


    make = tk.StringVar(selectMake)
    make.set(None)

    makeMenu = tk.OptionMenu(selectMake, make, *makes)
    makeMenu.pack(side=tk.LEFT)

    selectMake.pack()
    
    models =['Mustang', 'i8', 'Cruze']
    # commented this out for now bc only gives model1, model2.. etc in the dropdown
    # how can we make this list reflexive with all the models?
    # for i in range(11):
    #     models.append("model"+str(i))

    #create model label and menu in new frame
    selectModel = tk.Frame(partFinder)
    selectModelLabel = tk.Label(selectModel, text="Select Model: ")
    selectModelLabel.pack(side=tk.LEFT)

    model = tk.StringVar(selectModel)
    model.set(None)

    modelMenu = tk.OptionMenu(selectModel, model, *models)
    modelMenu.pack(side=tk.LEFT)

    selectModel.pack()
    """
    categories = ["Engine","Lights","Brakes", "Transmissions", "Windshield Wipers"]

    #create category label and menu in new frame
    selectCategory = tk.Frame(partFinder)
    selectCategoryLabel = tk.Label(selectCategory, text="Select Category (optional): ")
    selectCategoryLabel.pack(side=tk.LEFT)


    category = tk.StringVar(selectCategory)
    category.set(None)

    categoryMenu = tk.OptionMenu(selectCategory, category, *categories)
    categoryMenu.pack(side=tk.LEFT)

    selectCategory.pack()

    descriptions=["Brake Pads", "Headlights", "Brake Lights", "Coilovers"]

    #create description label and menu in new frame
    selectDescription = tk.Frame(partFinder)
    selectDescriptionLabel = tk.Label(selectDescription, text="Select Description (optional): ")
    selectDescriptionLabel.pack(side=tk.LEFT)

    description = tk.StringVar(selectDescription)
    description.set(None)

    descriptionMenu = tk.OptionMenu(selectDescription, description, *descriptions)
    descriptionMenu.pack(side=tk.LEFT)

    selectDescription.pack()

    def getProps():
        props = []
        props.append(year.get())
        props.append(make.get())
        props.append(model.get())
        if category.get():
            props.append(category.get())
        if description.get():
            props.append(description.get())
        print(props)
        mydb.searchPart(props)
        


    def clearProps():
        year.set(None)
        make.set(None)
        model.set(None)
        category.set(None)
        description.set(None)

    buttonGroup = tk.Frame(partFinder)

    searchButton = tk.Button(partFinder, text="Search", command=getProps)
    searchButton.pack(side=tk.RIGHT)

    clearButton = tk.Button(partFinder, text="Clear", command=clearProps)
    clearButton.pack(side=tk.RIGHT)

    buttonGroup.pack(side=tk.BOTTOM)

    partFinder.mainloop()

partWin()
