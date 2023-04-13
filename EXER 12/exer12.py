from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import *
from array import *
from time import *
import os
from reportlab.pdfgen import canvas
import csv

at = False
dotcom = False

et = False

presentInputFields = False
acceptBday = False
acceptEmail = False
dontacceptName = False




deletedIDList = []
#allDataList = [[]for n in range(30)]

allDataList = [['ID', 'Name', 'Address', 'Contact #', 'E-mail', 'Bday', 'Gender']]

allDataList2 = [[['Invoice No.', 'Prod ID', 'Prod Type', 'Prod Desc', 'Prod Quantity', 'Unit Price', 'Date']]]

invoice = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

# usedIndex = []
globID = 0
globIndex = 0


getColumn = 0
indexer = 0
delIndexer = 0

pid = None
ptype = None
pdesc = None
psupp = None
pquant = None
ptotalcost = None
pdate = None
currentDate = None
paddQuantity = None
pwindow = None
frame2 = None
frame3 = None
plabor = None
poverhead = None
pdesired = None


globRowInvoice = 0
globRowInvoiceNum = 0











#########################################################################################################################################################################

allPDataList = [['PID', 'PType', 'PDesc', 'Supplier', 'Total Quantity', 'Orders']]
allSDataList = [[['PID', 'PType', 'PDesc', 'Supplier', 'Quantity', 'Cost', 'Date', 'Orders']]]
threeDallPDataList = []     # 3D array in the form of 1D





globPID = 0
globPIndex = 0
globSIndex = 0
usedPIndex = []
getPColumn = 0

#########################################################################################################################################################################


def callback(event):
    # global gridddInfo
    # global usedIndex
    global globIndex
    global getColumn

    cid.set(allDataList[event.widget._values][0])   #When row is selected, it returns the values to the textfields(Entries)
    cname.set(allDataList[event.widget._values][1])
    cadrs.set(allDataList[event.widget._values][2])
    ccontact.set(allDataList[event.widget._values][3])
    cemail.set(allDataList[event.widget._values][4])
    cbday.set(allDataList[event.widget._values][5])
    cgender.set(allDataList[event.widget._values][6])

    globIndex = event.widget._values
    getColumn = event.widget._gettColumn
    # usedIndex.append(globIndex)

    createTable2()

    # print (globIndex)


   # gridddInfo = event.widget.grid_info()
    # print(usedIndex)
  #  print(gridddInfo['row'], gridddInfo['column'])


def createTable():
    global globIndex

    for d in frame1.winfo_children():   # delete row
        d.destroy()


    for i in range(len(allDataList)):
        for j in range(len(allDataList[i])):
            mgrid = Entry(frame1, width=18, bg='yellow')
            mgrid.insert(END, allDataList[i][j])
            mgrid._values = i
            mgrid._getIDtoDelete = i
            mgrid._gettColumn = j
            mgrid.grid(row=i+4, column=j+5)
            mgrid.bind("<Button-1>", callback)

def createTable2():

    for d in frame4.winfo_children():   # delete row
        d.destroy()

    for i in range(len(allDataList2[globIndex])):
        for j in range(len(allDataList2[globIndex][i])):
            mgrid = Entry(frame4, width=18, bg='yellow')
            mgrid.insert(END, allDataList2[globIndex][i][j])
            mgrid.grid(row=i+1, column=j+1)



def save():
    global presentInputFields
    global acceptBday
    global acceptEmail
    global dontacceptName
    global globID
    global allDataList
    global indexer




    if custemail.index("end") == 0 or custbday.index("end") == 0 or custcontact.index("end") == 0 or custadrs.index("end") == 0 or custname.index("end") == 0 or custgender.index("end") == 0:
        msgbox("Cannot save empty input fields!", "Record")
    else:
        presentInputFields = True



    if labelemail.cget("text") == "Bad e-mail":
        msgbox("Cannot save bad e-mail format!", "Record")

    if labelbday.cget("text") == "Bad Date Format":
        msgbox("Cannot save bad date format!", "Record")

    if labelbday.cget("text") == "No Minors!":
        msgbox("Cannot accept minors!", "Record")



    if labelemail.cget("text") == "Good e-mail" and labelbday.cget("text") == "Good Date Format" and presentInputFields == True and labelname.cget("text") != "Empty name input!" and labelemail.cget("text") != "Empty E-mail input!" and  labelbday.cget("text") != "Empty Date input!" and custadrs.index("end") != 0 and custcontact.index("end") != 0 and custgender.index("end") != 0:
        if not deletedIDList:
            msgbox("Save!", "Record")
            globID = globID + 1
            cid.set(str(globID))

            allDataList.append([cid.get(), cname.get(), cadrs.get(), ccontact.get(), cemail.get(), cbday.get(), cgender.get()]) 
            createTable()
        else:
            msgbox("Save!", "Record")
            globID = globID + 1
            cid.set(str(deletedIDList[0]))
            allDataList.append(
                [cid.get(), cname.get(), cadrs.get(), ccontact.get(), cemail.get(), cbday.get(), cgender.get()])
            createTable()
            deletedIDList.pop(0)
        allDataList2.append([['Invoice No.', 'Prod ID', 'Prod Type', 'Prod Desc', 'Prod Quantity', 'Unit Price', 'Date']])

        customersWrite()
        deletedIDWrite()
        ordersWrite()



          #  allDataList[indexer].append(cid.get())
          #  allDataList[indexer].append(cname.get())
          #  allDataList[indexer].append(cadrs.get())
          #  allDataList[indexer].append(ccontact.get())
         #   allDataList[indexer].append(cemail.get())
          #  allDataList[indexer].append(cbday.get())
          #  allDataList[indexer].append(cgender.get())

          #  indexer += 1


def delete():
    global allDataList
    global allDataList2
    global deletedIDList
    global globID

    msgbox("Delete!", "Record")
    deletedIDList.append(allDataList[globIndex][0])
    deletedIDList.sort()


    try:
        allDataList.pop(globIndex)
        allDataList2.pop(globIndex)
        globID -= 1
        # if usedIndex[-1] > 0 or NONE:
        #     createTable()
        # else:
        #     print("None")
        #     return

        createTable()
    except:
        print("None")

    customersWrite()
    ordersWrite()
    deletedIDWrite()

    


 # for i in range(len(deletedIDList)):  This just prints the values inside the deletedID list
      #  print(deletedIDList[i])

def update():
    global allDataList
    global globIndex
    global getColumn

    msgbox("Update!", "Record")
    allDataList[globIndex]= [cid.get(), cname.get(), cadrs.get(), ccontact.get(), cemail.get(), cbday.get(), cgender.get()]


    createTable()
    customersWrite()

# allDataList.append([cid.get(), cname.get(), cadrs.get(), ccontact.get(), cemail.get(), cbday.get(), cgender.get()])


def addproduct():

    pdate.set(currentDate.strftime('%m/%d/%Y'))

    finalUnitPrice = calculateUnitPrice()
    finalProductType = getProductType()
    finalProductDescription = getProductDescription()
    updateTableValues()
    count = 0
    for x in range(len(allDataList2[globIndex])):
        if allDataList2[globIndex][x][2] == finalProductType:
            if allDataList2[globIndex][x][3] == finalProductDescription:
                allDataList2[globIndex][x][4] = str(int(allDataList2[globIndex][x][4])+1)
                break
        count += 1
    if count == len(allDataList2[globIndex]):
        allDataList2[globIndex].append([invoice[globIndex], len(allDataList2[globIndex]), finalProductType, finalProductDescription, "1", finalUnitPrice, pdate.get()])
    createTable2()

    ordersWrite()
    stocksWrite()
    productsWrite()


def keyup(e):  # Checks the validity of the Customer e-mail
    global at
    global dotcom

    for x in range(len(custemail.get())):
        if custemail.get()[-1] == "@" and x > 1:
            at = True
        else:
            labelemail.config(text="Bad e-mail")

        if custemail.get()[-4:] == ".com" and x > 4 and at == True:
            dotcom = True
        else:
            labelemail.config(text="Bad e-mail")

        if at == True and dotcom == True and x > 13:
            labelemail.config(text="Good e-mail")
        else:
            labelemail.config(text="Bad e-mail")


    if custemail.index("end") == 0:
        labelemail.config(text="Empty E-mail input!")



def bdaySTR():
    meow = custbday.get()
    return meow

def valDOB():  # Checks the Bday Date Format
    try:
        strptime(bdaySTR(), '%m/%d/%Y')
        return True
    except ValueError:
        return False


def ageCalc(xAge):
    values = []
    for i in range(len(custbday.get())):
        values.append(custbday.get())

    values = xAge.split("/")
  #  month = int(values[0])
  #  day = int(values[1])
    year = int(values[2])

    today = date.today()
    years = today.year - year

    return years



def keybday(t):  # Checks the validity of the Customer Bday
    global et

    iscorrect = valDOB()



    if iscorrect == True:
        et = True
        labelbday.config(text="Good Date Format")
    else:
        labelbday.config(text="Bad Date Format")

    if et == True:
        bop = custbday.get()
        calculatedAge = ageCalc(bop)

        if calculatedAge < 18:
                labelbday.config(text="No Minors!")

    if len(custbday.get()) == 0:
        labelbday.config(text="Empty Date input!")





def keyname(u):
    if custname.index("end") == 0:
        labelname.config(text="Empty name input!")
    else:
        labelname.config(text = "Lastname, Firstname")



def msgbox(msg, titlebar):
    messagebox.showinfo(title=titlebar, message=msg)




##################################################################### PRODUCTS AREA #################################################################################################


def products():
    global pid, ptype, pdesc, psupp, pquant, ptotalcost, pdate, currentDate, paddQuantity, pwindow, frame2, frame3, plabor, poverhead, pdesired
    global allPDataList
    global globPID
    # global prodtype

    pwindow = Tk()
    pwindow.title("Products Form")
    pwindow.geometry("1820x600")
    pwindow.configure(bg="orange")

    frame2 = Frame(pwindow, width=100, highlightbackground='red', highlightthickness=3)
    frame2.grid(row=12, column=9, padx=20, pady=20, ipadx=20, ipady=20)

    StockInLabel = Label(pwindow, text="Stock In", width=15, height=1, bg="yellow")  # StockInLabel label
    StockInLabel .grid(column=9, row=13)

    frame3 = Frame(pwindow, width=100, highlightbackground='red', highlightthickness=3)
    frame3.grid(row=14, column=9, padx=20, pady=20, ipadx=20, ipady=20)





    labelstockin = Label(pwindow, text="New Products Stock-In", width=22, height=1, bg="yellow")
    labelstockin.config(font=("Courier", 10))
    labelstockin.grid(column=2, row=1)

    label = Label(pwindow, text="Product ID:", width=10, height=1, bg="yellow")  # Product ID label
    label.grid(column=1, row=2)  # Position of Product ID label
    pid = StringVar(pwindow)
    prodid = Entry(pwindow, textvariable=pid, state='disabled')  # Product ID Textfield
    prodid.grid(column=2, row=2)  # Position of Product ID Textfield

    label = Label(pwindow, text="Product Type:", width=15, height=1, bg="yellow")  # Product Type label
    label.grid(column=1, row=3)  # Position of Product Type  label
    ptype = StringVar(pwindow)
    prodtype = Entry(pwindow, textvariable=ptype)   # Product Type  Textfield
    prodtype.grid(column=2, row=3)

    label = Label(pwindow, text="Product Description:", width=15, height=1, bg="yellow")  # Product Description label
    label.grid(column=1, row=4)
    pdesc = StringVar(pwindow)
    prodDescrp = Entry(pwindow, textvariable = pdesc)  # Product Description Textfield
    prodDescrp.grid(column=2, row=4)

    label = Label(pwindow, text="Supplier:", width=16, height=1, bg="yellow")  # Supplier label
    label.grid(column=1, row=5)
    psupp = StringVar(pwindow)
    psupplier = Entry(pwindow, textvariable = psupp)  # Supplier Textfield
    psupplier.grid(column=2, row=5)

    # label = Label(window, text="Item Measure:", width=15, height=1, bg="yellow")  # Item Measure label
    # label.grid(column=1, row=6)
    #  pitemmeasure = ttk.Combobox(window, width=10)   # Item Measure Combobox
    #  pitemmeasure['values'] = ("Box", "Item2", "Item3")
    #  pitemmeasure.grid(column=2, row=6)

    label = Label(pwindow, text="Quantity:", width=15, height=1, bg="yellow")  # Quantity label
    label.grid(column=1, row=6)
    pquant = StringVar(pwindow)
    pquantity = Entry(pwindow, textvariable=pquant)  # Quantity  Textfield
    pquantity.grid(column=2, row=6)

    # +
    label = Label(pwindow, text="+", width=3, height=1, bg="yellow")  # + label
    label.grid(column=3, row=6)
    paddQuantity = StringVar(pwindow)
    plusquantity = Entry(pwindow, textvariable = paddQuantity)  # +  Textfield
    plusquantity.grid(column=4, row=6)

    label = Label(pwindow, text="Total Cost:", width=15, height=1, bg="yellow")  # Total Cost label
    label.grid(column=1, row=7)
    ptotcost = StringVar(pwindow)
    ptotalcost = Entry(pwindow, textvariable=ptotcost)  # Total Cost textfield
    ptotalcost.grid(column=2, row=7)


    currentDate = datetime.now()

    label = Label(pwindow, text="Date Received:", width=15, height=1, bg="yellow")  # Date Received label
    label.grid(column=1, row=8)
    pdate = StringVar(pwindow)
    pdateRcvd = Entry(pwindow, textvariable=pdate, state='disabled')  # Total Cost textfield
    pdateRcvd.grid(column=2, row=8)

    label = Label(pwindow, text="Labor Cost", width=15, height=1, bg="yellow")  # Date Received label
    label.grid(column=3, row=9)
    plabor = StringVar(pwindow)
    plaborcost = Entry(pwindow, textvariable=plabor)  # Total Cost textfield
    plaborcost.grid(column=4, row=9)
    plaborcost.bind("<KeyRelease>", keyplabor)

    label = Label(pwindow, text="Overhead Cost", width=15, height=1, bg="yellow")  # Date Received label
    label.grid(column=3, row=10)
    poverhead = StringVar(pwindow)
    poverheadcost = Entry(pwindow, textvariable=poverhead)  # Total Cost textfield
    poverheadcost.grid(column=4, row=10)
    poverheadcost.bind("<KeyRelease>", keypoverhead)



    label = Label(pwindow, text="Desired Profit", width=15, height=1, bg="yellow")  # Date Received label
    label.grid(column=3, row=11)
    pdesired = StringVar(pwindow)
    pdesiredprofit = Entry(pwindow, textvariable=pdesired)  # Total Cost textfield
    pdesiredprofit.grid(column=4, row=11)
    pdesiredprofit.bind("<KeyRelease>", keypdesired)

    psavebtn = Button(pwindow, text="New Product", command=newproduct)  #New Product Button
    psavebtn.grid(column=1, row=9)

    peditbtn = Button(pwindow, text="Stock In", command=stockin) #Stock In Button
    peditbtn.grid(column=1, row=10)

    productsRead()

    createSTable()

    stocksRead()
    LODread()

    createPTable()
    

def keyplabor(a):
    LODwrite()

def keypoverhead(a):
    LODwrite()

def keypdesired(a):
    LODwrite()



def Pcallback(event):

    # global usedPIndex
    global globPIndex
    # global getPColumn

    pid.set(allPDataList[event.widget._Pvalues][
                0])  # When row is selected, it returns the values to the textfields(Entries)
    ptype.set(allPDataList[event.widget._Pvalues][1])
    pdesc.set(allPDataList[event.widget._Pvalues][2])
    psupp.set(allPDataList[event.widget._Pvalues][3])
    pquant.set(allPDataList[event.widget._Pvalues][4])




    globPIndex = event.widget._Pvalues
    # getPColumn = event.widget._gettColumn
    # usedPIndex.append(globPIndex)

    # gridddInfo = event.widget.grid_info()
    print(usedPIndex)
    createSTable()
#  print(gridddInfo['row'], gridddInfo['column'])

def Scallback(event):

    global globSIndex


    
    globSIndex = event.widget._Svalues


    # gridddInfo = event.widget.grid_info()

#  print(gridddInfo['row'], gridddInfo['column'])


def newproduct():

    global allPDataList
    global globPID
    global threeDallPDataList

    globPID = globPID + 1
    pid.set(str(globPID))

    pdate.set(currentDate.strftime('%m/%d/%Y'))

    allPDataList.append([pid.get(), ptype.get(), pdesc.get(), psupp.get(), pquant.get(), "0"])
    createPTable()

    allSDataList.append([['PID', 'PType', 'PDesc', 'Supplier', 'Quantity', 'Cost', 'Date', 'Orders'],[pid.get(), ptype.get(), pdesc.get(), psupp.get(), pquant.get(),  ptotalcost.get(), pdate.get(), "0"]])
    createSTable()

    # z = 6

    # for a in range(len(allPDataList)):      #Inserts 2D  array values into 3D array
    #     threeDallPDataList.append([])
    #     for b in range(len(allPDataList)):
    #         threeDallPDataList[a].append([allPDataList[1]])
    #         for c in range(z):
    #             threeDallPDataList[a][b].append([allPDataList[1][0]])
    productsWrite()
    stocksWrite()


def stockin():

    pdate.set(currentDate.strftime('%m/%d/%Y'))

    allSDataList[globPIndex].append([pid.get(), ptype.get(), pdesc.get(), psupp.get(), paddQuantity.get(),  ptotalcost.get(), pdate.get(), "0"])
    createSTable()

    allPDataList[globPIndex][4] = str(int(allPDataList[globPIndex][4])+ int(paddQuantity.get()))
    createPTable()

    productsWrite()
    stocksWrite()

# def insert3DArray(event):   #Insert 3D array elements in second table
#     global threeDallPDataList


#     for f in range(len(threeDallPDataList)):
#         for g in range(len(threeDallPDataList[0])):
#             for h in range(len(threeDallPDataList[0][0])):
#                 mgrid2 = Entry(frame3, width=18, bg='yellow')
#                 mgrid2.insert(END, threeDallPDataList[f][g][h])
#                 mgrid2._3Dvalues = f
#                 mgrid2.grid(row=f + 4, column=g + 6)




            #print(threeDallPDataList[a][b][c], end=",")
            #   print("")
        #  print("")
    # print("--END--")



def calculateUnitPrice():
    partial = int (allSDataList[globPIndex][globSIndex][5]) / int (allSDataList[globPIndex][globSIndex][4])
    intLabor = float(plabor.get())
    intOverhead = float(poverhead.get())
    intDesired = float(pdesired.get())
    UnitPrice = partial + intLabor + intOverhead + intDesired
    return UnitPrice

def getProductType():
    prodType = allSDataList[globPIndex][globSIndex][1]
    return prodType

def getProductDescription():
    prodDesc = allSDataList[globPIndex][globSIndex][2]
    return prodDesc

def updateTableValues():
    allPDataList[globPIndex][4] = str(int(allPDataList[globPIndex][4])-1)
    allPDataList[globPIndex][5] = str(int(allPDataList[globPIndex][5])+1)
    allSDataList[globPIndex][globSIndex][4] = str(int(allSDataList[globPIndex][globSIndex][4])-1)
    allSDataList[globPIndex][globSIndex][7] = str(int(allSDataList[globPIndex][globSIndex][7])+1)
    createPTable()
    createSTable()



def createPTable():      #Function for creating table for the firstTable
    for widget in frame2.winfo_children():
        widget.destroy() 
    for t in range(len(allPDataList)):
        for u in range(len(allPDataList[0])):
            mgrid2 = Entry(frame2, width=18, bg='yellow')
            mgrid2.insert(END, allPDataList[t][u])
            mgrid2._Pvalues = t
            mgrid2.grid(row=t + 1, column=u + 1)
            mgrid2.bind("<Button-1>", Pcallback)


def createSTable():      #Function for creating table for the firstTable
    for widget in frame3.winfo_children():
        widget.destroy() 
    for t in range(len(allSDataList[globPIndex])):
        for u in range(len(allSDataList[globPIndex][t])):
            mgrid2 = Entry(frame3, width=18, bg='yellow')
            mgrid2.insert(END, allSDataList[globPIndex][t][u])
            mgrid2._Svalues = t
            mgrid2.grid(row=t + 1, column=u + 1)
            mgrid2.bind("<Button-1>", Scallback)










                      











    
























########################################################### END OF PRODUCTS AREA ############################################################################################

def customersWrite():
    sb = ""
    try:
        with open('customers.csv', 'w') as file:
            writer = csv.writer(file)

            for x in range(len(allDataList)):
                sb = sb + "-"
                sb = sb + ","

                for y in range(len(allDataList[x])):
                    sb = sb + str(allDataList[x][y])
                    sb = sb + ","
            writer.writerow([sb])    
    except:
        pass


def customersRead():
    global globID
    global allDataList
    global allDataList2

    

    try:
        a = -1
        with open('customers.csv') as file:
            allDataList.pop(0)
            globID -= 1
            reader = csv.reader(file)

            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")

                    for x in range(len(fromfile)):
                        if fromfile[x]:
                            if fromfile[x] == "-":
                                a = a + 1
                                allDataList.append([])
                                globID += 1
                            else:
                                allDataList[a].append(fromfile[x])


            

            # createTable()
    except:
        pass

def ordersWrite():
    sb = ""
    try:
        with open('customerOrders.csv', 'w') as file:
            
            writer = csv.writer(file)

            for x in range(len(allDataList2)):
                sb = sb + "+"
                sb = sb + ","  

                for y in range(len(allDataList2[x])):
                    sb = sb + "-"
                    sb = sb + ","

                    for z in range(len(allDataList2[x][y])):
                        sb = sb + str(allDataList2[x][y][z])
                        sb = sb + ","
            writer.writerow([sb])    
    except:
        pass

def ordersRead():
    global allDataList2
    try:
        a = -1
        b = -1
        with open('customerOrders.csv') as file:
            allDataList2 = []
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")

                    for x in range(len(fromfile)):
                        if fromfile[x]:
                            if fromfile[x] == "-":
                                b = b + 1
                                allDataList2[a].append([])
                            elif fromfile[x] == "+":
                                a = a + 1
                                b = -1
                                allDataList2.append([])
                            else:
                                allDataList2[a][b].append(fromfile[x])
  
    except:
        pass



def productsWrite():
    sb = ""
    try:
        with open('products.csv', 'w') as file:
            writer = csv.writer(file)

            for x in range(len(allPDataList)):
                sb = sb + "-"
                sb = sb + ","

                for y in range(len(allPDataList[x])):
                    sb = sb + str(allPDataList[x][y])
                    sb = sb + ","
            writer.writerow([sb])    
    except:
        pass


def productsRead():
    global globPID 
    global allPDataList
    global allSDataList

    

    try:
        a = -1
        with open('products.csv') as file:
            globPID -= 1
            allPDataList = []
            reader = csv.reader(file)

            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")

                    for x in range(len(fromfile)):
                        if fromfile[x]:
                            if fromfile[x] == "-":
                                a = a + 1
                                allPDataList.append([])
                                globPID  += 1
                            else:
                                allPDataList[a].append(fromfile[x])

            
            # createPTable()
    except:
        pass

def stocksWrite():
    sb = ""
    try:
        with open('stocks.csv', 'w') as file:

            writer = csv.writer(file)

            for x in range(len(allSDataList)):
                sb = sb + "+"
                sb = sb + "," 

                for y in range(len(allSDataList[x])):
                    sb = sb + "-"
                    sb = sb + "," 

                    for z in range(len(allSDataList[x][y])):
                        sb = sb + str(allSDataList[x][y][z])
                        sb = sb + ","
            writer.writerow([sb])    
    except:
        pass

def stocksRead():

    global allSDataList


    try:
        a = -1
        b = -1
        with open('stocks.csv') as file:
            allSDataList = []
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")
                    # print(fromfile)
                    for x in range(len(fromfile)):
                        if fromfile[x]:

                            if fromfile[x] == "-":
                                b = b + 1
                                allSDataList[a].append([])

                            elif fromfile[x] == "+":
                                a = a + 1
                                b = -1
                                allSDataList.append([])

                            else:
                                allSDataList[a][b].append(fromfile[x])
                            # print(fromfile[x])

            
    except Exception as error:
        # print(error)
        pass


def deletedIDWrite():
    sb = ""
    try:
        with open('deletedID.csv', 'w') as file:
            writer = csv.writer(file)
            for x in range(len(deletedIDList)):

                sb = sb + str(deletedIDList[x])
                sb = sb + ","

            writer.writerow([sb])    
    except:
        pass

def deletedIDread():
    global deletedIDList
    try:
        with open('deletedID.csv') as file:
            reader = csv.reader(file)

            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")

                    for x in range(len(fromfile)):
                        if fromfile[x]:
                            deletedIDList.append(int(fromfile[x]))

    except:
        pass


def LODwrite():
    sb = ""
    try:
        with open('costs.csv', 'w') as file:
            writer = csv.writer(file)

            sb += plabor.get()
            sb += ","
            sb += poverhead.get()
            sb += ","
            sb += pdesired.get()

            writer.writerow([sb])    
    except:
        pass

def LODread():
    try:
        with open('costs.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0:  
                    fromfile = line[0].split(",")
                    plabor.set(fromfile[0])
                    poverhead.set(fromfile[1])
                    pdesired.set(fromfile[2])
    except:
        pass    





def printInvoice():

  
    nowDate = strftime('%m/%d/%Y')
    
    custNumberr = allDataList[globIndex][0]
    custNamee = allDataList[globIndex][1]
    custAddress = allDataList[globIndex][2]
    custContactt = allDataList[globIndex][3]
    
   # custInvoiceNum = allDataList2[globIndex][0]
  
    
    
    
    

    c = canvas.Canvas("invoice.pdf")
    c.drawString(40,800, "Cerberod Shop")
    c.drawString(40,788, "#56 Vinewood Boulevard")
    c.drawString(40,776, "Los Santos, 9500")
    c.drawString(40,764, "Contact: 555-2471")

    c.drawString(440,800, "Invoice")
    c.drawString(440,788, "Date: " + nowDate )
    c.drawString(440,776, "Invoice#: " )
    c.drawString(440,764, "Customer#: " + custNumberr)

    c.line(0,745,600,745)

    c.drawString(40,730, "Bill To")
    c.drawString(40,708, custNamee )
    c.drawString(40,686, custAddress)
    c.drawString(40,664, custContactt)

    c.line(0,650,600,650)

    c.drawString(80,624, "Product")
    c.drawString(170,624, "Description")
    c.drawString(330,624, "Quantity")
    c.drawString(430,624, "Unit Price")

    c.line(0,605,600,605)

    y = 580
    y2 = 560
    y3 = 540

    subtotall = 0
    taxy = 0
    allTotal = 0
 
    for z in range(len(allDataList2[globIndex])):
       if z != 0: 
        c.drawString(80,y ,str(allDataList2[globIndex][z][2]))
        c.drawString(170,y ,str(allDataList2[globIndex][z][3]))
        c.drawString(330,y ,str(allDataList2[globIndex][z][4]))
        c.drawString(430,y ,str(allDataList2[globIndex][z][5]))
        c.drawString(490,776 ,str(allDataList2[globIndex][z][0]))

        quanty = float(allDataList2[globIndex][z][4])
        unitPricey = float(allDataList2[globIndex][z][5])

        subtotall += quanty * unitPricey
        stringSubtotall = str(subtotall)

        taxy = float(stringSubtotall) * 0.12
        allTotal = float(stringSubtotall) + taxy

        stringTaxy = str(taxy)
        stringAllTotal = str(allTotal)
        
        
        

    

        y = y - 20
        y2 = y2 - 20
        y3 = y3 - 20






    c.drawString(330,y ,"SubTotal: ")
    c.drawString(330,y2 ,"Tax: ")
    c.drawString(330,y3 ,"Total: ")

    c.drawString(430,y ,stringSubtotall)
    c.drawString(430,y2 ,stringTaxy)
    c.drawString(430,y3 ,stringAllTotal)

   

    
        
           # c.drawString(90,y ,str(allDataList2[z][x][1]))
           # c.drawString(140,580,str(allDataList2[z][x][2]))
           # c.drawString(210,580,str(allDataList2[z][x][3]))
            
            
        
   # c.drawString(80,580, "Product")


    c.save()
    os.startfile("invoice.pdf")





































window = Tk()  # The main GUI form
window.title("Customer Registration System")
window.geometry("1820x600")
window.configure(bg="orange")


containerFrame = Frame(window)

















menubar = Menu(window)  # Creates a MenuBar (upper left)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)  # File menubar
filemenu.add_command(label="Products", command=products)
filemenu.add_command(label="Orders")
filemenu.add_separator()
filemenu.add_command(label="Close", command=window.quit)

window.config(menu=menubar)  # Activates the menu bar

label = Label(window, text="Customer Registration System", width=30, height=1, bg="yellow")
label.config(font=("Courier", 10))
label.grid(column=2, row=1)

label = Label(window, text="Customer ID:", width=10, height=1, bg="yellow")  # Customer ID label
label.grid(column=1, row=2)  # Position of Customer ID label
cid = StringVar()
custid = Entry(window, textvariable=cid, state='disabled')  # Customer ID Textfield
custid.grid(column=2, row=2)  # Position of Customer ID Textfield


label = Label(window, text="Customer name:", width=15, height=1, bg="yellow")  # Customer name label
label.grid(column=1, row=3)  # Position of Customer name label
labelname = Label(window, text="Lastname, Firstname", width=20, height=1, bg="yellow")  # Customer name label instruction
labelname.grid(column=3, row=3)
cname = StringVar()
custname = Entry(window, textvariable=cname)  # Customer name Textfield
custname.grid(column=2, row=3)
custname.bind("<KeyRelease>", keyname)

label = Label(window, text="Customer Address:", width=15, height=1, bg="yellow")  # Customer Address label
label.grid(column=1, row=4)
cadrs = StringVar()
custadrs = Entry(window, textvariable=cadrs)  # Customer Address Textfield
custadrs.grid(column=2, row=4)

label = Label(window, text="Customer Contact #:", width=16, height=1, bg="yellow")  # Customer Contact # label
label.grid(column=1, row=5)
ccontact = StringVar()
custcontact = Entry(window, textvariable=ccontact)  # Customer Contact # Textfield
custcontact.grid(column=2, row=5)

label = Label(window, text="Customer E-mail:", width=15, height=1, bg="yellow")  # Customer E-mail label
label.grid(column=1, row=6)
labelemail = Label(window, text="[a-z] @ [a-z].com", width=15, height=1,
                   bg="yellow")  # Customer E-mail label instruction
labelemail.grid(column=3, row=6)
cemail = StringVar()
custemail = Entry(window, textvariable=cemail)  # Customer E-mail Textfield
custemail.grid(column=2, row=6)
custemail.bind("<KeyRelease>", keyup)

label = Label(window, text="Customer Bday:", width=15, height=1, bg="yellow")  # Customer Bday label
label.grid(column=1, row=7)
labelbday = Label(window, text="mm/dd/yyyy", width=15, height=1, bg="yellow")  # Customer Bday label instruction
labelbday.grid(column=3, row=7)
cbday = StringVar()
custbday = Entry(window, textvariable=cbday)  # Customer Bday Textfield
custbday.grid(column=2, row=7)
custbday.bind("<KeyRelease>", keybday)

label = Label(window, text="Customer Gender:", width=15, height=1, bg="yellow")  # Customer Gender label
label.grid(column=1, row=8)
cgender = StringVar()
custgender = ttk.Combobox(window, width=8, textvariable=cgender)  # Customer Gender Combobox
custgender['values'] = ("Male", "Female")
custgender.grid(column=2, row=8)


savebtn = Button(text="Save", command=save)
savebtn.grid(column=1, row=9)

deletebtn = Button(text="Delete", command=delete)
deletebtn.grid(column=2, row=9)

updatebtn = Button(text="Update", command=update)
updatebtn.grid(column=3, row=9)

addproductbtn = Button(text="Add Product", command=addproduct)
addproductbtn.grid(column=3, row=10)

printInvoiceBtn = Button(text="Print Invoice", command=printInvoice)
printInvoiceBtn.grid(column=3, row=11)




lst = [[1,'ralphy','koronadal', '22856', 'ralphy@gmail.com', '01/02/2001',], [2,'poopsy','koronadal2', '228562', 'ralphy2@gmail.com', '01/02/2000',], [3,'ralphy3','koronadal3', '228563', 'ralphy3@gmail.com', '01/02/1999',]]





frame1 = Frame(window, width=100, highlightbackground='red', highlightthickness=3)
frame1.grid(row=11, column=10, padx=20, pady=20, ipadx=20, ipady=20)

label = Label(window, text = "costumer products")
label.grid(row = 12, column = 10)

frame4 = Frame(window, width=100, highlightbackground='red', highlightthickness=3)
frame4.grid(row=13, column=10, padx=20, pady=20, ipadx=20, ipady=20)




#labelRows = []
#for m in range(1):
  #  labelCols = ['ID', 'Name', 'Address', 'Contact #', 'E-mail', 'Bday', 'Gender']
  #  for o in range(7):
    #    labelEntry = Entry(frame1, width=18, bg='yellow')
    #    labelEntry.grid(row=m+3, column=o+5)
  #      labelEntry.insert(END, labelCols[o])

   #     labelCols.append(labelEntry)
  #  labelRows.append(labelCols)


customersRead()
createTable2()

ordersRead()

deletedIDread()

createTable()











window.mainloop()



