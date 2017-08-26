#Python 3.6.1
#appJar 0.07

from appJar import gui

def AddBills(btn):
    Water = app.getEntry("Water")
    Electric = app.getEntry("Electric")
    Internet = app.getEntry("Internet")
    VehicleLoan = app.getEntry("Vehicle Loan")
    CreditCard = app.getEntry("Credit Card")
    Mortgage = app.getEntry("Mortgage")
    VehicleInsurance = app.getEntry("Vehicle Insurance")

    app.setTextArea("Bill Sum", Water + Electric + Internet +
    VehicleLoan + CreditCard + Mortgage + VehicleInsurance)

app = gui("Bill Manager", "500x500")

app.setFont(20)
app.setBg("grey")

app.addNumericEntry("Water", 0, 2)
app.addNumericEntry("Electric", 1, 2)
app.addNumericEntry("Internet", 2, 2)
app.addNumericEntry("Vehicle Loan", 3, 2)
app.addNumericEntry("Credit Card", 4, 2)
app.addNumericEntry("Mortgage", 5, 2)
app.addNumericEntry("Vehicle Insurance", 6, 2)
app.addButton("Add Bills", AddBills, 7, 2)
app.addTextArea("Bill Sum", 8, 2)

app.setEntryDefault("Water", "Water")
app.setEntryDefault("Electric", "Electric")
app.setEntryDefault("Internet", "Internet")
app.setEntryDefault("Vehicle Loan", "Vehicle Loan")
app.setEntryDefault("Credit Card", "Credit Card")
app.setEntryDefault("Mortgage", "Mortgage")
app.setEntryDefault("Vehicle Insurance", "Vehicle Insurance")

app.addCheckBox("Water", 0, 0)
app.addCheckBox("Electric", 1, 0)
app.addCheckBox("Internet", 2, 0)
app.addCheckBox("Vehicle Loan", 3, 0)
app.addCheckBox("Credit Card", 4, 0)
app.addCheckBox("Mortgage", 5, 0)
app.addCheckBox("Vehicle Insurance", 6, 0)

def update_meter():

    billList = [app.getCheckBox("Water"), app.getCheckBox("Electric"), app.getCheckBox("Internet"),
               app.getCheckBox("Vehicle Loan"), app.getCheckBox("Credit Card"),
               app.getCheckBox("Mortgage"), app.getCheckBox("Vehicle Insurance")]

    bill_value = [0]

    for bill in billList:
        if bill is True:
            bill_value.append(14.2857142857)
    addValues = sum(bill_value)
    app.setMeter("Progress", addValues)

app.registerEvent(update_meter)

app.addMeter("Progress")
app.setMeterFill("Progress", "green")

app.go()
