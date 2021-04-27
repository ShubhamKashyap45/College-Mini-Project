from tkinter import *
import sqlite3 as db


root = Tk()
root.geometry("800x600")
root.title("Car Rental Receipt")

# Create a database or connect to one
connect1 = db.connect('Receipt_Database.db')

# Create a cursor
cur = connect1.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS DATA
(
    Date TEXT,
    Receipt TEXT,
    Company TEXT,
    Representative TEXT,  
    Location TEXT,
    Phone TEXT,
    VIN TEXT,
    Make TEXT,
    Year TEXT,
    Colour TEXT,
    Registration TEXT,
    Model TEXT,
    Mileage TEXT
)''')
cur.close()
connect1.commit()
connect1.close()



def getvalue():
    connect1 = db.connect('Receipt_Database.db')
    cur = connect1.cursor()
    cur.execute("Insert into DATA values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                % (user_date.get(), user_receipt.get(), company_entry.get(),
                   res_entry.get(), location_entry.get(), phone_entry1.get(), vin_entry.get(),
                   make_entry.get(), year_entry.get(), color_entry.get(), reg_entry.get(),
                   model_entry.get(), mileage_entry.get()))
    cur.close()
    connect1.commit()
    cur.close()

    print("\n")
    print("Personal Information")
    print("\n")

    print("Date:", user_date.get())
    print("Receipt:", user_receipt.get())
    print("\n")

    print("Rental Company Info")
    print("Company:", company_entry.get())
    print("Representative:", res_entry.get())
    print("Location:", location_entry.get())
    print("City/State/Zip:", city_entry1.get())
    print("Phone:", phone_entry1.get())
    print("\n")

    print("Lessee Info")
    print("Name:", name_entry.get())
    print("License #:", lic_entry.get())
    print("Address:", add_entry.get())
    print("City/State/Zip:", city_entry2.get())
    print("Phone:", phone_entry2.get())
    print("\n")

    print("VIN:", vin_entry.get())
    print("Make:", model_entry.get())
    print("Year:", year_entry.get())
    print("Colour:", color_entry.get())
    print("Registration:", reg_entry.get())
    print("Model:", model_entry.get())
    print("Mileage:", mileage_entry.get())
    print("\n")

    print("Payment Method:")
    print("\n")

    print("Check No:", Check_entry.get())
    print("Credit No:", Credit.get())
    print("Other", othervar.get())
    print("\n")
    print("Representative Name:", Rep_var.get())


# Car Rental Reciept Heading
text_label = Label(text="CAR RENTAL RECEIPT", font="lucida 15 bold")
text_label.grid(pady=10, row=0, column=2)

# 1st part Labels
date = Label(root, text="Date:").grid(sticky="w", row=1, column=0)
receipt = Label(root, text="Receipt #:").grid(sticky="w", row=2, column=0)

# 1st part vars
datevalue = StringVar()
receiptvalue = StringVar()

# 1st part Entry widgets
user_date = Entry(root, textvariable = datevalue)
user_date.grid(row=1, column=1)

user_receipt = Entry(root, textvariable = receiptvalue)
user_receipt.grid(row=2, column=1)

# 2nd part Heading Label
company_info = Label(root, text="Rental Company Info", font="lucida 10 bold")
company_info.grid(sticky="w", pady=3, row=3, column=0)

lessee_info = Label(root, text="Lessee Info", font="lucida 10 bold")
lessee_info.grid(sticky="w", pady=3, padx=10, row=3, column=2)

# 2nd part vars

# Rental Company Info
companyvar = StringVar()
representativevar = StringVar()
locationvar = StringVar()
city1var = StringVar()
phone1var = StringVar()

# Lessee Info
namevar = StringVar()
licvar = StringVar()
addvar = StringVar()
city2var = StringVar()
phone2var= StringVar()



# 2nd part Label

# Rental Company Info
Label(root, text="Company:").grid(sticky="w", row=4, column=0)
Label(root, text="Representative:").grid(sticky="w", row=5, column=0)
Label(root, text="Location:").grid(sticky="w", row=6, column=0)
Label(root, text="City/State/Zip:").grid(sticky="w", row=7, column=0)
Label(root, text="Phone:").grid(sticky="w", row=8, column=0)


# Lessee Info
Label(root, text="Name:").grid(padx=10, sticky="w", row=4, column=2)
Label(root, text="License #:").grid(padx=10, sticky="w", row=5, column=2)
Label(root, text="Address:").grid(padx=10, sticky="w", row=6, column=2)
Label(root, text="City/State/Zip:").grid(padx=10, sticky="w", row=7, column=2)
Label(root, text="Phone:").grid(padx=10, sticky="w", row=8, column=2)


# 2nd part Entry

# Rental Company Info
company_entry = Entry(root, textvariable = companyvar)
company_entry.grid(row=4, column=1)

res_entry = Entry(root, textvariable = representativevar)
res_entry.grid(row=5, column=1)

location_entry = Entry(root, textvariable = locationvar)
location_entry.grid(row=6, column=1)

city_entry1 = Entry(root, textvariable = city1var)
city_entry1.grid(row=7, column=1)

phone_entry1 = Entry(root, textvariable = phone1var)
phone_entry1.grid(row=8, column=1)

# Lessee Info
name_entry = Entry(root, textvariable = namevar)
name_entry.grid(row=4, column=3)

lic_entry = Entry(root, textvariable = licvar)
lic_entry.grid(row=5, column=3)

add_entry = Entry(root, textvariable = addvar)
add_entry.grid(row=6, column=3)

city_entry2 = Entry(root, textvariable = city2var)
city_entry2.grid(row=7, column=3)

phone_entry2 = Entry(root, textvariable = phone2var)
phone_entry2.grid(row=8, column=3)

# 3rd part heading

# Vehicle Information
vehicle_info = Label(root, text="Vehicle Information", font="lucida 12 bold")
vehicle_info.grid(pady=10, sticky="w", row=9, column=2)


# Vehicle Information Label
Label(root, text="VIN:").grid(sticky="w", row=10, column=0)
Label(root, text="Make:").grid(sticky="w", row=11, column=0)
Label(root, text="Year:").grid(sticky="w", row=12, column=0)
Label(root, text="Colour:").grid(sticky="w", row=13, column=0)


Label(root, text="Registration #:").grid(padx=10, sticky="w", row=10, column=2)
Label(root, text="Model:").grid(padx=10, sticky="w", row=11, column=2)
Label(root, text="Mileage:").grid(padx=10, sticky="w", row=12, column=2)


# 3rd part vars
vinvar = StringVar()
makevar = StringVar()
yearvar = StringVar()
colorvar = StringVar()
regvar = StringVar()
modelvar = StringVar()
mileagevar = StringVar()


# Vehicle Information Entry
vin_entry = Entry(root, textvariable = vinvar)
vin_entry.grid(row=10, column=1)

make_entry = Entry(root, textvariable = makevar)
make_entry.grid(row=11, column=1)

year_entry = Entry(root, textvariable = yearvar)
year_entry.grid(row=12, column=1)

color_entry = Entry(root, textvariable = colorvar)
color_entry.grid(row=13, column=1)

reg_entry = Entry(root, textvariable = regvar)
reg_entry.grid(row=10, column=3)

model_entry = Entry(root, textvariable = modelvar)
model_entry.grid(row=11, column=3)

mileage_entry = Entry(root, textvariable = mileagevar)
mileage_entry.grid(row=12, column=3)

# Grid Box Label
Label(root, text="VIN", font="lucida 10 bold").grid(row=14, column=0)
Label(root, text="Cost/Day", font="lucida 10 bold").grid(row=14, column=1)
Label(root, text="# of Days", font="lucida 10 bold").grid(row=14, column=2)
Label(root, text="Additional Cost", font="lucida 10 bold").grid(row=14, column=3)
Label(root, text="Line Total", font="lucida 10 bold").grid(row=14, column=4)


# Grid Box vars
vin1 = StringVar()
vin2 = StringVar()
vin3 = StringVar()

Cost1 = StringVar()
Cost2 = StringVar()
Cost3 = StringVar()

days1 = StringVar()
days2 = StringVar()
days3 = StringVar()

additional1 = StringVar()
additional2 = StringVar()
additional3 = StringVar()

line1 = StringVar()
line2 = StringVar()
line3 = StringVar()

# Grid Box Entry
vin1_entry = Entry(root,width=22, textvariable = vin1).grid(row=15, column=0, columnspan=1)
vin2_entry = Entry(root,width=22, textvariable = vin2).grid(row=16, column=0)
vin3_entry = Entry(root,width=22, textvariable = vin3).grid(row=17, column=0)

Cost1_entry = Entry(root, textvariable = Cost1).grid(row=15, column=1)
Cost2_entry = Entry(root, textvariable = Cost2).grid(row=16, column=1)
Cost3_entry = Entry(root, textvariable = Cost3).grid(row=17, column=1)

days1_entry = Entry(root, width=37, textvariable = days1).grid(row=15, column=2, columnspan=1)
days2_entry = Entry(root, width=37, textvariable = days2).grid(row=16, column=2)
days3_entry = Entry(root, width=37, textvariable = days3).grid(row=17, column=2)

additional1_entry = Entry(root, textvariable = additional1).grid(row=15, column=3)
additional2_entry = Entry(root, textvariable = additional2).grid(row=16, column=3)
additional3_entry = Entry(root, textvariable = additional3).grid(row=17, column=3)

line1_entry = Entry(root, textvariable = line1).grid(row=15, column=4)
line2_entry = Entry(root, textvariable = line2).grid(row=16, column=4)
line3_entry = Entry(root, textvariable = line3).grid(row=17, column=4)

# Payment Method Label
Label(root, text="Payment Method:", font="lucida 10 bold").grid(sticky="w", row=18, column=0)
Label(root, text="Subtotal:").grid(sticky="w", row=18, column=3)
Label(root, text="Tax:").grid(sticky="w", row=19, column=3)
Label(root, text="Total:").grid(sticky="w", row=20, column=3)
Label(root, text="Amount Paid:", font="lucida 10 bold").grid(sticky="w", row=21, column=3)

subtotal = StringVar()
tax = StringVar()
total = StringVar()
Amountpaid = StringVar()

subtotal_entry = Entry(root, textvariable = subtotal).grid(row=18, column=4)
tax_entry = Entry(root, textvariable = tax).grid(row=19, column=4)
total_entry = Entry(root, textvariable = total).grid(row=20, column=4)
Amountpaid_entry = Entry(root, textvariable = Amountpaid).grid(row=21, column=4)

# Creating vars for checkbox
cash_var = IntVar()
check_var = IntVar()
credit_var = IntVar()
other_var = IntVar()

Credit = StringVar()
othervar = StringVar()
CheckNo = StringVar()

# Creating Checkbuttons
Checkbutton(root, text="Cash", variable=cash_var).grid(sticky="w", row=19, column=0)
Checkbutton(root, text="Check No:", variable=check_var).grid(sticky="w", row=19, column=1)
Checkbutton(root, text="Credit No.", variable=credit_var).grid(sticky="w", row=20, column=0)
Checkbutton(root, text="Other", variable=other_var).grid(sticky="w", row=21, column=0)


Check_entry = Entry(root, textvariable = CheckNo)
Check_entry.grid(sticky="w",row=19, column=2)
Credit_entry = Entry(root, textvariable = Credit).grid(sticky="w", row=20, column=1)
Other_entry = Entry(root, textvariable = othervar).grid(sticky="w", row=21, column=1)

# Representative Name
Label(root, text="Representative Name:").grid(pady=5, sticky="w", row=22, column=3)


Rep_var = StringVar()

# Entry
Rep_entry = Entry(root, textvariable = Rep_var).grid(row=22, column=4)


# Submit button
submit_button = Button(root, text="Submit", padx=13, bg="black", fg="white", command=getvalue)
submit_button.grid(pady=15, row=22, column=1)



# End of code
root.mainloop()