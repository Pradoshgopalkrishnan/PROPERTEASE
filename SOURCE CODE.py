from tkinter import *
import os
from dotenv import load_dotenv
import random
import mysql.connector as m
print("Current Working Directory:", os.getcwd())


dotenv_path = dotenv_path = "C:\\Users\\HP\\Propertease\\.env"

if os.path.exists(dotenv_path):
    print("✅ Found .enq file!")
    load_dotenv(dotenv_path)
else:
    print("❌ .env file not found at", dotenv_path)

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASS:", os.getenv("DB_PASS"))
print("DB_NAME:", os.getenv("DB_NAME"))
r=Tk()
d = m.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cur = d.cursor()


ebi_id = '0001'
pradosh_id = '0007'
ebi_passcode = 'sparky@2020'
pradosh_passcode = 'stretchy@molecules'



ebi_id = '0001'
pradosh_id = '0007'
ebi_passcode = 'sparky@2020'
pradosh_passcode = 'stretchy@molecules'


# Adding the base window to the root window
def faf():
    """Hides all frames or widgets in the main window."""
    for frames in r.winfo_children():
        frames.grid_forget()

def toggle_password(entry_widget, show_pass_var):
    if show_pass_var.get():
        entry_widget.config(show='')  # Show password
    else:
        entry_widget.config(show='*')  # Hide password
def firstfunction():
    faf()
    global e
    e = Frame(r, bg="white")
    e.grid(sticky="nsew")
    r.title('PropertEase')

    l = Label(e, text='Welcome to PropertEase', font=("Helvetica", 24, "bold"), fg="dark blue", bg="white")
    l.grid(row=0, column=0, columnspan=3, pady=(20, 10), padx=10, sticky="n")

    b1 = Button(e, text='Customer', padx=40, pady=20, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=customer)
    b2 = Button(e, text='Real Estate Agent', padx=40, pady=20, fg='white', bg='#5F6368', font=("Arial", 14, "bold"),
                command=start_agent)
    b3 = Button(e, text='Admin', padx=40, pady=20, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=start_admin)

    b1.grid(row=1, column=0, padx=10, pady=10)
    b2.grid(row=1, column=1, padx=10, pady=10)
    b3.grid(row=1, column=2, padx=10, pady=10)

    r.grid_columnconfigure(0, weight=1)
    r.grid_columnconfigure(1, weight=1)
    r.grid_columnconfigure(2, weight=1)
    r.grid_rowconfigure(1, weight=1)


def customer():
    faf()
    global f
    e.grid_forget()
    f = Frame(r, bg="white")
    f.grid(sticky="nsew")

    cl = Label(f, text='Customer Selection', font=("Helvetica", 20, "bold"), fg="white", bg="#007ACC")
    cl.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

    cb1 = Button(f, text='New Customer', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                 command=newcustomer)
    cb2 = Button(f, text='Existing Customer', padx=40, pady=15, fg='white', bg='#4285F4', font=("Arial", 14, "bold"),
                   command=oldcustomer)
    cb3=Button(f,text='Back',padx=40,pady=15,bg='#6d7985',fg='white',command=firstfunction)
    cb3.grid(row=2,column=1,sticky='ew')

    cb1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    cb2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    f.grid_columnconfigure(0, weight=1)
    f.grid_columnconfigure(1, weight=1)


def oldcustomer():
    faf()
    global k
    global entry2
    global enter
    f.grid_forget()
    k = Frame(r, bg="white")
    k.grid(padx=20, pady=20, sticky="nsew")

    l = Label(k, text='Enter your customer ID', font=("Arial", 16, "bold"), bg="white", fg="black")
    enter = Entry(k, width=30, font=("Arial", 14))

    l2 = Label(k, text='Enter your password', font=("Arial", 16, "bold"), bg="white", fg="black")
    entry2 = Entry(k, width=30, font=("Arial", 14), show='*')
    uu = BooleanVar()
    go = Checkbutton(k, text='show password ', variable=uu, command=lambda: toggle_password(entry2, uu))
    go.grid(row=9)
    b1 = Button(k, text='OK', padx=40, pady=15, fg='white', bg='#4285F4', font=("Arial", 14, "bold"),
                command=verification)
    cb3=Button(k,text='back',padx=40,pady=15,bg='#6d7985',fg='white',command=customer)

    l.grid(row=0, column=0, pady=10, sticky="w")
    enter.grid(row=1, column=0, pady=10, sticky="ew")
    l2.grid(row=2, column=0, pady=10, sticky="w")
    entry2.grid(row=3, column=0, pady=10, sticky="ew")
    b1.grid(row=4, column=0, pady=20, sticky="ew")
    cb3.grid(row=5,column=0,sticky='ew')

def newcustomer():
    faf()
    global t
    global entry2
    global enter
    f.grid_forget()
    t = Frame(r, bg="white")
    t.grid(padx=20, pady=20, sticky="nsew")

    l = Label(t, text='Enter your name', font=("Arial", 16, "bold"), bg="white", fg="black")
    enter = Entry(t, width=40, font=("Arial", 14))
    l2 = Label(t, text='Enter Your Password', font=("Arial", 16, "bold"), bg="white", fg="black")
    entry2 = Entry(t, width=40, font=("Arial", 14), show='*')
    uu=BooleanVar()
    b1 = Button(t, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"), command=cid)
    cb3=Button(t,text='back',padx=40,pady=15,bg='#6d7985',fg='white',command=customer)
    go=Checkbutton(t,text='show password ',variable=uu,command=lambda:toggle_password(entry2,uu))
    go.grid(row=6,column=0)

    l.grid(row=0, column=0, pady=10, sticky="w")
    enter.grid(row=1, column=0, pady=10, sticky="ew")
    l2.grid(row=2, column=0, pady=10, sticky="w")
    entry2.grid(row=3, column=0, pady=10, sticky="ew")
    b1.grid(row=4, column=0, pady=20, sticky="ew")
    cb3.grid(row=5,column=0,sticky='ew')

def cid():
    faf()
    global passcode
    passcode = entry2.get()
    t.grid_forget()
    global i
    a = random.randrange(0, 9999)
    i = Frame(r, bg="white")
    i.grid(padx=20, pady=20)

    l = Label(i, text='Your customer ID is', font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    l2 = Label(i, text=str(a), font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    l3 = Label(i, text='Your account password is ', font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    l4 = Label(i, text=str(passcode), font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    b1 = Button(i, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=customer)

    l.grid(row=0, column=0, pady=10, sticky="w")
    l2.grid(row=1, column=0, pady=10, sticky="w")
    l3.grid(row=2, column=0, pady=10, sticky="w")
    l4.grid(row=3, column=0, pady=10, sticky="w")
    b1.grid(row=4, column=0, pady=20, sticky="ew")

    cur.execute("INSERT INTO customer (cname, cno, password) VALUES (%s, %s, %s);", (enter.get(), a, passcode))
    d.commit()


def verification():
    faf()
    global k4
    k3 = entry2.get()
    k4 = enter.get()
    cur.execute('SELECT password FROM customer WHERE cno=%s', (k4,))
    b1 = cur.fetchone()

    if b1 is not None:
        a1 = b1[0]
        if a1 == k3:
            k.grid_forget()
            manage_customer(k4)
        else:
            show_error_message()
    else:
        show_error_message()


def manage_customer(cno):
    faf()
    global j
    global kk
    if 'kk' in globals():
        kk.destroy()
    j = Frame(r, bg="white")
    j.grid(sticky="nsew")

    b1 = Button(j, text='Manage', padx=40, pady=15, fg='white', bg='#4285F4', font=("Arial", 14, "bold"),
                command=lambda: manage(cno))
    b2 = Button(j, text='Sell', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"), command=sell)
    b3 = Button(j, text='Buy', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=lambda: buy(cno))
    b4 = Button(j, text='Exit', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=finalcustomer)

    b1.grid(row=0, column=0, pady=10, sticky="ew")
    b2.grid(row=1, column=0, pady=10, sticky="ew")
    b3.grid(row=2, column=0, pady=10, sticky="ew")
    b4.grid(row=3, column=0, pady=10, sticky="ew")


# Showing an error message and retrying
def show_error_message():
    faf()
    k.grid_forget()
    global j1
    if 'j1' in globals():
        j1.destroy()
    j1 = Frame(r, bg="white")
    j1.grid(padx=20, pady=20, sticky="nsew")

    l1 = Label(j1, text='Oops! Wrong password for the customer ID, try again', fg='red', font=("Arial", 14, "bold"))
    b1 = Button(j1, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=lambda: retry_oldcustomer(j1))

    l1.grid(row=0, column=0, pady=10)
    b1.grid(row=1, column=0, pady=10, sticky="ew")


def retry_oldcustomer(error_frame):
    error_frame.grid_forget()
    oldcustomer()


def manage(cno):
    cur.execute('SELECT * FROM properties WHERE scno=%s', (cno,))
    properties = cur.fetchall()

    j.grid_forget()

    j5 = Frame(r, bg='white')
    j5.grid(sticky="nsew")
    b1 = Button(j5, text='OK', padx=40, pady=15, bg='blue', fg='white', font='Arial',
                command=lambda: manage_customer(cno))
    cb3=Button(j5,text='back',padx=40,pady=15,bg='#6d7985',fg='white',command=lambda:manage_customer(k4))
    cb3.grid(row=91,column=91)    
    b1.grid(row=90, column=90)

    headers = ["Property ID", "Rooms", "Bathrooms", "Kitchen", "Price", "Seller Contact", "Buyer Contact", "Status",
               "Location"]

    for col, header in enumerate(headers):
        header_label = Label(j5, text=header, font=("Arial", 12, "bold"), bg='white', anchor='w')
        header_label.grid(row=0, column=col, padx=10, pady=10)

    for row, property in enumerate(properties, start=1):
        for col, value in enumerate(property):
            value_label = Label(j5, text=value, font=("Arial", 12), bg='white', anchor='w')
            value_label.grid(row=row, column=col, padx=10, pady=5, sticky='w')


def buy(cno):
    faf()
    global b4, buy_frame, buy_entry, customer_no
    customer_no = cno  # Store the customer number globally so it can be accessed in other functions

    cur.execute('SELECT ano, rooms, bathrooms, kitchen, price, scno, bcno, status, location, propertyid FROM properties WHERE status="sell" AND scno!=%s', (cno,))
    properties = cur.fetchall()

    buy_frame = Frame(r, bg='white')
    buy_frame.grid(sticky="nsew")

    headers = ["Agent ID", "Rooms", "Bathrooms", "Kitchen", "Price", "Seller Contact", "Buyer Contact", "Status", "Location", "Property ID"]

    for col, header in enumerate(headers):
        header_label = Label(buy_frame, text=header, font=("Arial", 12, "bold"), bg='white', anchor='center')
        header_label.grid(row=0, column=col, padx=10, pady=10)

    # Initialize row counter
    row = 1

    for property in properties:
        for col, value in enumerate(property):
            value_label = Label(buy_frame, text=value, font=("Arial", 12), bg='white', anchor='center')
            value_label.grid(row=row, column=col, padx=10, pady=5, sticky='ew')
        row += 1  # Increment row for the next property

    # Adding entry box for property ID
    Label(buy_frame, text="Enter the Property ID you wish to buy:", font=("Arial", 14), bg='white').grid(row=row, column=0, padx=10, pady=10, sticky='w')
    buy_entry = Entry(buy_frame, width=10, font=("Arial", 14))
    buy_entry.grid(row=row, column=1, padx=10, pady=10, sticky='w')

    b4 = Button(buy_frame, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=lambda: validate_property(cno))
    b4.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    b6=Button(buy_frame,text='Search by sq.feet',padx=40,pady=15,bg='blue',fg='white',command=search)
    b6.grid(row=row+1,column=3,columnspan=2)
    b7=Button(buy_frame,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=lambda:manage_customer(k4))
    b7.grid(row=90,column=3)

def validate_property(cno):
    global buy_frame, buy_entry
    property_id = buy_entry.get()

    cur.execute('SELECT * FROM properties WHERE propertyid=%s', (property_id,))
    property = cur.fetchone()

    if property:
        buy_frame.grid_forget()
        show_agent_details(property_id,cno)
    else:
        show_property_error(cno)

def search():
    # Clear all frames
    faf()
    
    # Create the search frame and widgets
    sf = Frame(r, bg="white")
    sf.grid(sticky="nsew")
    
    # Labels and Entry fields for min and max square footage
    l1 = Label(sf, text="Input the minimum square feet you need", font=("Arial", 14), bg="white")
    e1 = Entry(sf, width=20, font=("Arial", 14))
    l2 = Label(sf, text="Input the maximum amount of square feet", font=("Arial", 14), bg="white")
    e2 = Entry(sf, width=20, font=("Arial", 14))
    
    # Placing widgets in the grid
    l1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    e1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    l2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    e2.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    
    # Search button with command to run the search and display results
    search_button = Button(sf, text="Search", padx=40, pady=15, fg="white", bg="#007ACC", font=("Arial", 14, "bold"),
                           command=lambda: display_search_results(e1.get(), e2.get(), sf))
    search_button.grid(row=4, column=0, pady=20, sticky="ew")
    
    # Back button to return to the customer management menu
    back_button = Button(sf, text="Back", padx=40, pady=15, fg="white", bg="#6d7985", font=("Arial", 14, "bold"),
                         command=lambda: manage_customer(k4))
    back_button.grid(row=5, column=0, pady=20, sticky="ew")

def display_search_results(min_sqft, max_sqft, frame):
    # Clear the search frame for displaying results
    frame.grid_forget()
    
    # Validate user input
    try:
        min_sqft = int(min_sqft)
        max_sqft = int(max_sqft)
    except ValueError:
        error_message("Please enter valid numeric values for square footage.")
        return
    
    # Execute the SQL query to filter properties
    cur.execute("SELECT * FROM properties WHERE square_feet BETWEEN %s AND %s", (min_sqft, max_sqft))
    results = cur.fetchall()
    
    # Create results display frame
    results_frame = Frame(r, bg="white")
    results_frame.grid(sticky="nsew")
    
    # If no results found
    if not results:
        Label(results_frame, text="No properties found in this range.", font=("Arial", 14), bg="white", fg="red").grid(padx=20, pady=20)
    else:
        # Column headers
        headers = ["Property ID", "Rooms", "Bathrooms", "Kitchen", "Price", "Seller Contact", "Buyer Contact", "Status", "Location", "Square Feet"]
        for col, header in enumerate(headers):
            Label(results_frame, text=header, font=("Arial", 12, "bold"), bg="white").grid(row=0, column=col, padx=10, pady=10)

        # Display each property in a new row
        for row_idx, property_data in enumerate(results, start=1):
            for col_idx, value in enumerate(property_data):
                Label(results_frame, text=value, font=("Arial", 12), bg="white").grid(row=row_idx, column=col_idx, padx=10, pady=5)

    # OK button to go back
    Button(results_frame, text="OK", padx=40, pady=15, fg="white", bg="#34A853", font=("Arial", 14, "bold"),
           command=lambda: manage_customer(k4)).grid(pady=20, sticky="ew")
    
    
    
    

    
def show_property_error(cno):
    faf()
    global error_frame
    error_frame = Frame(r, bg="white")
    error_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(error_frame, text="Property doesn't exist. Please try again.", font=("Arial", 14, "bold"), bg="white",
              fg="red")
    b = Button(error_frame, text='OK', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=lambda: buy(cno))

    l.grid(row=0, column=0, pady=20)
    b.grid(row=1, column=0, pady=10, sticky="ew")


def show_agent_details(property_id, cno):
    global o3, e1, customer_no
    # Fetch the agent number (ano) from the properties table based on the property ID
    cur.execute('SELECT ano FROM properties WHERE propertyid=%s;', (property_id,))
    agent_no = cur.fetchone()

    if agent_no:
        # Now, fetch the agent details using the agent number
        cur.execute('SELECT ano, aname, acontact FROM agent WHERE ano=%s;', (agent_no[0],))
        agent_data = cur.fetchall()

        o3 = Frame(r, bg="white")
        o3.grid(padx=20, pady=20, sticky="nsew")

        headers = ['Agent ID', 'Agent Name', 'Contact No.']
        for col, header in enumerate(headers):
            l = Label(o3, text=header, font=("Arial", 12, "bold"), bg="white", fg="black", anchor='center')
            l.grid(row=0, column=col, padx=10, pady=10, sticky="ew")

        # If the agent_data is empty, we have to check the relationship
        if not agent_data:
            Label(o3, text="No agent found for this property", font=("Arial", 12), bg="white", fg="black", anchor='center').grid(row=1, column=0, columnspan=3, pady=10, padx=10)
        else:
            for row, agent in enumerate(agent_data, start=1):
                for col, value in enumerate(agent):
                    vl = Label(o3, text=value, font=("Arial", 12), bg="white", fg="black", anchor='center')
                    vl.grid(row=row, column=col, padx=10, pady=5, sticky="ew")

        final_row = len(agent_data) + 1  # Ensure the button is placed below the agent data
        b1 = Button(o3, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=lambda: manage_customer(cno))
        b1.grid(row=final_row, column=0, columnspan=3, pady=20, sticky="ew")

    else:
        show_property_error(cno)



def sell():
    faf()
    global o1, rno, bno, kno, pno, lno, lpp, k4  # Include k4 in globals
    j.grid_forget()
    o1 = Frame(r, bg='white')
    o1.grid(padx=10, pady=10)

    l2 = Label(o1, text='Enter the number of rooms in your property', font=("Arial", 14), bg='white', fg='black')
    rno = Entry(o1, width=30, font=("Arial", 14))

    l3 = Label(o1, text='Enter the number of bathrooms in your property', font=("Arial", 14), bg='white', fg='black')
    bno = Entry(o1, width=30, font=("Arial", 14))

    l4 = Label(o1, text='Enter the number of kitchens in your property', font=("Arial", 14), bg='white', fg='black')
    kno = Entry(o1, width=30, font=("Arial", 14))

    l5 = Label(o1, text='Enter the price at which you want to sell your property', font=("Arial", 14), bg='white', fg='black')
    pno = Entry(o1, width=30, font=("Arial", 14))

    l6 = Label(o1, text='Enter the location where your property is located', font=("Arial", 14), bg='white', fg='black')
    lno = Entry(o1, width=30, font=("Arial", 14))

    b12 = Label(o1, text='Enter the square feet of the property you are selling', fg='black', bg='white', font=('Arial', 14))
    lpp = Entry(o1, width=40, font=('Arial', 14))

    b1 = Button(o1, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=propertyid)
    b9 = Button(o1, text='Back', padx=40, pady=15, fg='white', bg='#6d7985', command=lambda: manage_customer(k4))

    # Place the widgets accordingly
    l2.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    rno.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    l3.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    bno.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    l4.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    kno.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    l5.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    pno.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    l6.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    lno.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    b12.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    lpp.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    b1.grid(row=6, column=0, pady=20)
    b9.grid(row=6, column=1, pady=20)


    
def propertyid():
    global gu, o2, k4  # Include k4 in globals
    if not rno.get() or not bno.get() or not kno.get() or not pno.get() or not lno.get() or not lpp.get():
        show_empty_fields_error()
        return

    gu = random.randrange(1000, 9999)  # Ensure a 4-digit property ID
    o1.grid_forget()
    o2 = Frame(r, bg='white')
    o2.grid(padx=20, pady=20, sticky="nsew")

    l1 = Label(o2, text='Your property ID is:', font=("Arial", 16), bg="white", fg="black", anchor='w')
    l2 = Label(o2, text=str(gu), font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    b1 = Button(o2, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=agent)

    l1.grid(row=0, column=0, pady=10, sticky="w")
    l2.grid(row=1, column=0, pady=10, sticky="w")
    b1.grid(row=2, column=0, pady=20, sticky="ew")

    # Use k4 (logged-in customer's number)
    cur.execute(
        'INSERT INTO properties (ano, rooms, bathrooms, kitchen, price, scno, bcno, status, location, propertyid, square_feet) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (None, rno.get(), bno.get(), kno.get(), pno.get(), k4, None, "sell", lno.get(), gu, lpp.get()))
    d.commit()


def show_empty_fields_error():
    faf()
    error_frame = Frame(r, bg="white")
    error_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(error_frame, text='Please input all the fields', font=("Arial", 14, "bold"), bg="white", fg="red")
    b = Button(error_frame, text='OK', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=sell)

    l.grid(row=0, column=0, pady=20)
    b.grid(row=1, column=0, pady=10, sticky="ew")


def agent():
    global o3, e1
    cur.execute('SELECT ano, aname, acontact FROM agent;')
    agent_data = cur.fetchall()

    o2.grid_forget()
    o3 = Frame(r, bg="white")
    o3.grid(padx=20, pady=20, sticky="nsew")

    headers = ['Agent no.', 'Agent name', 'Contact no.']
    for col, header in enumerate(headers):
        l = Label(o3, text=header, font=("Arial", 12, "bold"), bg="white", fg="black", anchor='w')
        l.grid(row=0, column=col, padx=10, pady=10, sticky="w")

    # Initialize row counter
    row = 1

    for agent in agent_data:
        for col, value in enumerate(agent):
            vl = Label(o3, text=value, font=("Arial", 12), bg="white", fg="black", anchor='w')
            vl.grid(row=row, column=col, padx=10, pady=5, sticky="w")
        row += 1  # Increment row for the next agent

    l1 = Label(o3, text='Give the agent no. of your choice', font=("Arial", 14), bg="white", fg="black", anchor='w')
    e1 = Entry(o3, width=4, font=("Arial", 14))
    b1 = Button(o3, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"), command=insertingsql)

    l1.grid(row=row, column=0, pady=10, sticky="w")
    e1.grid(row=row + 1, column=0, pady=10, sticky="w")
    b1.grid(row=row + 2, column=0, pady=20, sticky="ew")


def insertingsql():
    global kk
    o3.grid_forget()
    kk = Frame(r, bg="white")
    kk.grid(padx=20, pady=20, sticky="nsew")

    ll = Label(kk, text='Your property has been successfully listed for sale', font=("Arial", 16), bg="white",
               fg="green")
    b1 = Button(kk, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=lambda: manage_customer(k4))

    ll.grid(row=0, column=0, pady=20, sticky="w")
    b1.grid(row=1, column=0, pady=20, sticky="ew")

    # Update the ano (Agent ID) in the properties table
    cur.execute(
        'UPDATE properties SET ano = %s WHERE propertyid = %s',
        (e1.get(), gu)  # Use agent ID (e1.get()) and property ID (gu)
    )
    d.commit()



def finalcustomer():
    global nn
    faf()
    nn = Frame(r, bg='white')
    nn.grid()
    ooo = Label(nn, text='Thank you For using PropertEase', font=("Arial", 14), bg="white", fg="black", anchor='w')
    b1 = Button(nn, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=destroy_customer)

    ooo.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")


def destroy_customer():
    r.destroy()


# Start Agent Function
def start_agent():
    global p
    faf()
    e.grid_forget()
    p = Frame(r, bg="light gray")
    p.grid(padx=20, pady=20, sticky="nsew")

    l3 = Button(p, text='Want to be agent?', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=c_admin)
    l4 = Button(p, text='Agent already?', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                command=old_agent)
    lm=Button(p,text='EXIT',padx=40,pady=15,font='Arial',command=f_agent,bg='red')
    l3.grid(row=0, column=0, pady=10, sticky="ew")
    l4.grid(row=1, column=0, pady=10, sticky="ew")
    lm.grid(row=2,column=0,pady=10,sticky='ew')
    b7=Button(p,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=firstfunction)
    b7.grid(row=4,column=0)
    p.grid_columnconfigure(0, weight=1)
def f_agent():
    faf()
    poo=Frame(r)
    poo.grid(sticky='nsew')
    ooo = Label(poo, text='Thank you For using PropertEase', font=("Arial", 14), bg="white", fg="black", anchor='w')
    b1 = Button(poo, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=destroy_customer)

    ooo.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")

# Admin contact details
def c_admin():
    faf()
    global p
    if 'p' in globals():
        p.grid_forget()
    p = Frame(r, bg="white")
    p.grid(padx=20, pady=20, sticky="nsew")

    l3 = Label(p, text='Contact these admins', font=("Arial", 16, "bold"), bg="white", fg="black")
    l4 = Label(p, text='Name=Ebenezer, contact no.=XXXXXXXXXXXXXXXX', font=("Arial", 14), bg="white", fg="black",
               anchor='w')
    l5 = Label(p, text='Name=Pradosh, contact no.=XXXXXXXXXXXXXXXXX', font=("Arial", 14), bg="white", fg="black",
               anchor='w')
    b1 = Button(p, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=start_agent)
    b7=Button(p,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=start_agent)
    b7.grid(row=4,column=0)
    l3.grid(row=0, column=0, pady=10, sticky="ew")
    l4.grid(row=1, column=0, pady=10, sticky="w")
    l5.grid(row=2, column=0, pady=10, sticky="w")
    b1.grid(row=3, column=0, pady=20, sticky="ew")


# Agent login
def old_agent():
    faf()
    global x
    if 'x' in globals():
        x.grid_forget()
    x = Frame(r, bg="white")
    x.grid(padx=20, pady=20, sticky="nsew")

    global aenter
    global paenter

    l1 = Label(x, text='Enter your Agent ID /ano', font=("Arial", 16, "bold"), bg="white", fg="black")
    aenter = Entry(x, width=30, font=("Arial", 14))

    l2 = Label(x, text='Enter your agent password', font=("Arial", 16, "bold"), bg="white", fg="black")
    paenter = Entry(x, width=30, font=("Arial", 14), show='*')
    uu=BooleanVar()
    go=Checkbutton(x,text='show password ',variable=uu,command=lambda:toggle_password(paenter,uu))
    b1 = Button(x, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=verify_agent)
    b7=Button(x,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=start_agent)
    b7.grid(row=6,column=0)
    l1.grid(row=0, column=0, pady=10, sticky="w")
    aenter.grid(row=1, column=0, pady=10, sticky="ew")
    l2.grid(row=2, column=0, pady=10, sticky="w")
    paenter.grid(row=3, column=0, pady=10, sticky="ew")
    b1.grid(row=4, column=0, pady=20, sticky="ew")
    go.grid(row=5)

# Verifying agent's password
def verify_agent():
    faf()
    agent_id = aenter.get()
    agent_pass = paenter.get()

    cur.execute('SELECT agent_password FROM agent WHERE ano=%s', (agent_id,))
    result = cur.fetchone()

    if result and str(result[0]) == agent_pass:
        x.grid_forget()
        agent_handling()
    else:
        agent_error_message()


# Agent handling after successful login
def agent_handling():
    faf()
    global b
    b = Frame(r, bg="white")
    b.grid(padx=20, pady=20, sticky="nsew")

    la = Label(b, text='Who is buying the property (bcno)?', font=("Arial", 14), bg="white", fg="black", anchor='w')
    ea = Entry(b, width=30, font=("Arial", 14))
    lb = Label(b, text='Who is selling the property (scno)?', font=("Arial", 14), bg="white", fg="black", anchor='w')
    eb = Entry(b, width=30, font=("Arial", 14))
    lc = Label(b, text='Enter the status of the property (sold/sell)', font=("Arial", 14), bg="white", fg="black",
               anchor='w')
    ec = Entry(b, width=5, font=("Arial", 14))
    ld = Label(b, text='Enter the property ID you want to sell', font=("Arial", 14), bg="white", fg="black", anchor='w')
    ed = Entry(b, width=4, font=("Arial", 14))

    la.grid(row=0, column=0, pady=10, sticky="w")
    ea.grid(row=1, column=0, pady=10, sticky="ew")
    lb.grid(row=2, column=0, pady=10, sticky="w")
    eb.grid(row=3, column=0, pady=10, sticky="ew")
    lc.grid(row=4, column=0, pady=10, sticky="w")
    ec.grid(row=5, column=0, pady=10, sticky="ew")
    ld.grid(row=6, column=0, pady=10, sticky="w")
    ed.grid(row=7, column=0, pady=10, sticky="ew")

    b1 = Button(b, text='Submit', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                command=lambda: finalize_sale(ea.get(), eb.get(), ec.get(), ed.get(), aenter.get()))
    b1.grid(row=8, column=0, pady=20, sticky="ew")


# Finalizing the sale process
def finalize_sale(buyer_cno, seller_cno, status, property_id, agentid):
    faf()
    cur.execute('''UPDATE properties 
                   SET bcno = %s, status = %s 
                   WHERE scno = %s AND propertyid = %s and ano=%s''',
                (buyer_cno, status, seller_cno, property_id, agentid))
    d.commit()

    cur.execute('SELECT * FROM properties WHERE scno = %s AND propertyid = %s AND ano = %s',
                (seller_cno, property_id, agentid))
    re = cur.fetchone()

    if re is None:
        show_agent_error_frame()
    else:
        show_agent_success_frame()
# Error if agent inputs wrong details
def show_agent_error_frame():
    faf()
    global error_frame
    error_frame = Frame(r, bg="white")
    error_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(error_frame, text='No matching property found. Please check the scno and property ID.',
              font=("Arial", 14, "bold"), bg="white", fg="red")
    b = Button(error_frame, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=lambda: retry_agent_handling(error_frame))

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


# Successful sale process message
def show_agent_success_frame():
    faf()
    global success_frame
    success_frame = Frame(r, bg="white")
    success_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(success_frame, text='Property sale completed successfully!',
              font=("Arial", 14, "bold"), bg="white", fg="green")
    b = Button(success_frame, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
               command=firstfunction)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def retry_agent_handling(error_frame):
    error_frame.grid_forget()
    agent_handling()


# Error message if agent inputs wrong ID/pass
def agent_error_message():
    faf()
    x.grid_forget()
    global j2
    if 'j2' in globals():
        j2.destroy()
    j2 = Frame(r, bg="white")
    j2.grid(padx=20, pady=20, sticky="nsew")

    l1 = Label(j2, text='Oops! Wrong password for the Agent ID, try again', fg='red', font=("Arial", 14, "bold"))
    b1 = Button(j2, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=lambda: retry_agent(j2))

    l1.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")


def retry_agent(j2):
    j2.grid_forget()
    old_agent()


def start_admin():
    faf()
    e.grid_forget()
    ad = Frame(r, bg="white")
    ad.grid(padx=20, pady=20, sticky="nsew")

    l = Label(ad, text='Admin login', font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    l2 = Label(ad, text='What is your admin id', font=("Arial", 14), bg="white", fg="black", anchor='w')
    l3 = Label(ad, text='What is your admin passcode', font=("Arial", 14), bg="white", fg="black", anchor='w')
    t = Entry(ad, width=10, font=("Arial", 14))
    t2 = Entry(ad, width=10, font=("Arial", 14), show='*')
    mm=BooleanVar()
    t5=Checkbutton(ad,text='show password ',variable=mm,command=lambda:toggle_password(t2,mm))
    b1 = Button(ad, text='OK', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=lambda: verify_admin(t.get(), t2.get(), ad))
    b7=Button(ad,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=firstfunction)
    b7.grid(row=7,column=0)

    l.grid(row=0, column=0, pady=10, sticky="w")
    l2.grid(row=1, column=0, pady=10, sticky="w")
    t.grid(row=2, column=0, pady=10, sticky="ew")
    l3.grid(row=3, column=0, pady=10, sticky="w")
    t2.grid(row=4, column=0, pady=10, sticky="ew")
    b1.grid(row=5, column=0, pady=20, sticky="ew")
    t5.grid(row=6,column=0,pady=10,sticky='ew')

def verify_admin(admin_id, admin_passcode, ad_frame):
    if (admin_id == ebi_id and admin_passcode == ebi_passcode) or (
            admin_id == pradosh_id and admin_passcode == pradosh_passcode):
        ad_frame.grid_forget()
        admin_success()
    else:
        admin_error()


def admin_error():
    faf()
    global j3
    j3 = Frame(r, bg="white")
    j3.grid(padx=20, pady=20, sticky="nsew")

    l1 = Label(j3, text='Incorrect Admin ID or Passcode. Please try again.', fg='red', font=("Arial", 14, "bold"))
    b1 = Button(j3, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=lambda: retry_admin(j3))

    l1.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")


def retry_admin(j3):
    j3.grid_forget()
    start_admin()


def admin_success():
    faf()
    ads = Frame(r, bg="white")
    ads.grid(padx=20, pady=20, sticky="nsew")

    l = Label(ads, text='What do you want to do?', font=("Arial", 16, "bold"), bg="white", fg="black", anchor='w')
    b1 = Button(ads, text='Add agent', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                command=add_agent)
    b2 = Button(ads, text='Remove agent', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=del_agent)
    b3 = Button(ads, text='Remove customer', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=del_customer)
    b4 = Button(ads, text='Use Admin Commands', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
                command=admin_com)
    b5 = Button(ads, text='☠️NUKE☠️', padx=40, pady=15, fg='white', bg='#FF0000', font=("Arial", 14, "bold"),
                command=adm_nuke)
    cb3=Button(ads,text='Exit',padx=40,pady=15,bg='Black',fg='white',command=finalcustomer)
    cb4=Button(ads,text='Back',padx=40,pady=15,bg='#6d7985',fg='white',command=firstfunction)
    cb4.grid(row=2,column=1,sticky='ew')

    l.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")
    b2.grid(row=2, column=0, pady=10, sticky="ew")
    b3.grid(row=3, column=0, pady=10, sticky="ew")
    b4.grid(row=4, column=0, pady=10, sticky="ew")
    b5.grid(row=5, column=0, pady=10, sticky="ew")
    cb3.grid(row=6,column=0,pady=10,sticky='ew')
    cb4.grid(row=7,column=0,pady=10,sticky='ew')
    ads.grid_columnconfigure(0, weight=1)


def add_agent():
    faf()
    fo = Frame(r, bg="white")
    fo.grid(padx=20, pady=20, sticky="nsew")

    l = Label(fo, text='What is the Name of the agent', font=("Arial", 14), bg="white", fg="black", anchor='w')
    h1 = Entry(fo, width=50, font=("Arial", 14))
    l2 = Label(fo, text='What is the ID of the agent (agentid)', font=("Arial", 14), bg="white", fg="black", anchor='w')
    h2 = Entry(fo, width=10, font=("Arial", 14))
    l3 = Label(fo, text='What is the contact number of the agent', font=("Arial", 14), bg="white", fg="black",
               anchor='w')
    h3 = Entry(fo, width=15, font=("Arial", 14))
    l4 = Label(fo, text='What is the agent passcode', font=("Arial", 14), bg="white", fg="black", anchor='w')
    h4 = Entry(fo, width=20, font=("Arial", 14))

    b1 = Button(fo, text='Submit', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                command=lambda: insert_agent(h1.get(), h2.get(), h3.get(), h4.get(), fo))
    b7=Button(fo,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=admin_success)

    l.grid(row=0, column=0, pady=10, sticky="w")
    h1.grid(row=0, column=1, pady=10, sticky="ew")
    l2.grid(row=1, column=0, pady=10, sticky="w")
    h2.grid(row=1, column=1, pady=10, sticky="ew")
    l3.grid(row=2, column=0, pady=10, sticky="w")
    h3.grid(row=2, column=1, pady=10, sticky="ew")
    l4.grid(row=3, column=0, pady=10, sticky="w")
    h4.grid(row=3, column=1, pady=10, sticky="ew")
    b1.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")
    b7.grid(row=5,column=3)

def insert_agent(name, agentid, contact, passcode, frame):
    faf()
    try:
        cur.execute("INSERT INTO agent (aname, ano, acontact, agent_password) VALUES (%s, %s, %s, %s)",
                    (name, agentid, contact, passcode))
        d.commit()
        frame.grid_forget()
        success_message("Agent added successfully!")
    except Exception as e:
        frame.grid_forget()
        error_message(f"Failed to add agent: {e}")


def success_message(message):
    faf()
    sm = Frame(r, bg="white")
    sm.grid(padx=20, pady=20, sticky="nsew")

    l = Label(sm, text=message, font=("Arial", 14, "bold"), bg="white", fg="green", anchor='w')
    b = Button(sm, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
               command=admin_success)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def error_message(message):
    faf()
    em = Frame(r, bg="white")
    em.grid(padx=20, pady=20, sticky="nsew")

    l = Label(em, text=message, font=("Arial", 14, "bold"), bg="white", fg="red", anchor='w')
    b = Button(em, text='OK', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=admin_success)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def del_agent():
    faf()
    w = Frame(r, bg="white")
    w.grid(padx=20, pady=20, sticky="nsew")

    l = Label(w, text='Enter the agent ID of the agent you want to delete:', font=("Arial", 14), bg="white", fg="black",
              anchor='w')
    q = Entry(w, width=10, font=("Arial", 14))
    b = Button(w, text='Delete', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=lambda: delete_or_show_error(q.get()))
    b7=Button(w,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=admin_success)
    b7.grid(row=3,column=0)
    l.grid(row=0, column=0, pady=10, sticky="w")
    q.grid(row=1, column=0, pady=10, sticky="ew")
    b.grid(row=2, column=0, pady=20, sticky="ew")

    def delete_or_show_error(agent_id):
        cur.execute('SELECT * FROM agent WHERE ano=%s', (agent_id,))
        agent = cur.fetchone()

        if agent:
            delete_agent(agent_id)
        else:
            agent_not_found()

    def agent_not_found():
        w.grid_forget()
        error_frame = Frame(r, bg="white")
        error_frame.grid(padx=20, pady=20, sticky="nsew")

        l1 = Label(error_frame, text='Agent not found. Please check the ID and try again.', fg='red',
                   font=("Arial", 14, "bold"), anchor='w')
        b1 = Button(error_frame, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437',
                    font=("Arial", 14, "bold"),
                    command=del_agent)

        l1.grid(row=0, column=0, pady=10, sticky="w")
        b1.grid(row=1, column=0, pady=10, sticky="ew")

    def delete_agent(agent_id):
        cur.execute('DELETE FROM agent WHERE ano=%s', (agent_id,))
        d.commit()
        w.grid_forget()
        success_frame = Frame(r, bg="white")
        success_frame.grid(padx=20, pady=20, sticky="nsew")

        l2 = Label(success_frame, text=f'Agent with ID {agent_id} deleted successfully.', fg='green',
                   font=("Arial", 14, "bold"), anchor='w')
        b2 = Button(success_frame, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                    command=firstfunction)

        l2.grid(row=0, column=0, pady=10, sticky="w")
        b2.grid(row=1, column=0, pady=10, sticky="ew")


def del_customer():
    faf()
    de = Frame(r, bg="white")
    de.grid(padx=20, pady=20, sticky="nsew")

    l = Label(de, text='Enter the customer ID you want to delete:', font=("Arial", 14), bg="white", fg="black",
              anchor='w')
    po = Entry(de, width=10, font=("Arial", 14))
    b = Button(de, text='Delete', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=lambda: delete_customer(po.get(), de))
    b7=Button(de,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=admin_success)
    b7.grid(row=3,column=0)
    l.grid(row=0, column=0, pady=10, sticky="w")
    po.grid(row=1, column=0, pady=10, sticky="ew")
    b.grid(row=2, column=0, pady=20, sticky="ew")


def delete_customer(cno, de_frame):
    cur.execute('SELECT * FROM customer WHERE cno=%s', (cno,))
    go = cur.fetchone()

    if go is None:
        no_cus(de_frame)
    else:
        cus_sus(cno, de_frame)


def no_cus(de_frame):
    de_frame.grid_forget()
    fu = Frame(r, bg="white")
    fu.grid(padx=20, pady=20, sticky="nsew")

    le = Label(fu, text='Customer does not exist. Try again.', font=("Arial", 14, "bold"), bg="white", fg="red",
               anchor='w')
    bu = Button(fu, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
                command=del_customer)

    le.grid(row=0, column=0, pady=10, sticky="w")
    bu.grid(row=1, column=0, pady=10, sticky="ew")


def cus_sus(cno, de_frame):
    cur.execute('DELETE FROM customer WHERE cno = %s', (cno,))
    d.commit()

    de_frame.grid_forget()
    do = Frame(r, bg="white")
    do.grid(padx=20, pady=20, sticky="nsew")

    lo = Label(do, text='Customer removed successfully.', font=("Arial", 14, "bold"), bg="white", fg="green",
               anchor='w')
    b = Button(do, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
               command=admin_success)

    lo.grid(row=0, column=0, pady=10, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def admin_com():
    faf()
    global op
    op = Frame(r, bg="white")
    op.grid(padx=20, pady=20, sticky="nsew")

    lo = Label(op, text='Enter the command you want to perform:', font=("Arial", 14), bg="white", fg="black",
               anchor='w')
    en = Entry(op, width=90, font=("Arial", 14))
    b = Button(op, text='Execute', padx=40, pady=15, fg='white', bg='#007ACC', font=("Arial", 14, "bold"),
               command=lambda: execute_command(en.get(), op))
    b7=Button(op,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=admin_success)
    b7.grid(row=3,column=0)
    lo.grid(row=0, column=0, pady=10, sticky="w")
    en.grid(row=1, column=0, pady=10, sticky="ew")
    b.grid(row=2, column=0, pady=20, sticky="ew")


def execute_command(command, frame):
    try:
        # Strip any leading/trailing spaces and execute the command
        command = command.strip()
        cur.execute(command)

        # If it's a SELECT query, fetch and display the results
        if command.lower().startswith('select'):
            results = cur.fetchall()
            display_results(results, frame)
        else:
            d.commit()
            show_command_success(frame)
    except Exception as e:
        # Print the error for debugging and show the error message in the UI
        print(f"Error: {e}")
        show_invalid_command(frame)
def display_results(results, frame):
    # Clear the frame before displaying the results
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a new frame to display the results
    result_frame = Frame(frame, bg="white")
    result_frame.grid(padx=20, pady=20, sticky="nsew")

    # If there are no results, display a message
    if not results:
        Label(result_frame, text="No results found.", font=("Arial", 14, "bold"), bg="white", fg="red").grid(row=0, column=0, pady=20, sticky="w")
        return

    # Display column headers from cur.description (if you have column names available)
    headers = [desc[0] for desc in cur.description]
    for col, header in enumerate(headers):
        Label(result_frame, text=header, font=("Arial", 12, "bold"), bg='white', anchor='w').grid(row=0, column=col, padx=10, pady=10)

    # Display the query results row by row
    for row_index, row_data in enumerate(results, start=1):
        for col_index, col_data in enumerate(row_data):
            Label(result_frame, text=col_data, font=("Arial", 12), bg='white', anchor='w').grid(row=row_index, column=col_index, padx=10, pady=5, sticky='w')

    # Add an OK button to return to the admin command screen
    Button(result_frame, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"), command=admin_success).grid(row=row_index + 1, column=0, columnspan=len(headers), pady=20, sticky="ew")

def show_command_success(frame):
    frame.grid_forget()
    success_frame = Frame(r, bg="white")
    success_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(success_frame, text='Command executed successfully!',
              font=("Arial", 14, "bold"), bg="white", fg="green")
    b = Button(success_frame, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
               command=admin_success)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def show_invalid_command(frame):
    frame.grid_forget()
    error_frame = Frame(r, bg="white")
    error_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(error_frame, text='Invalid command', font=("Arial", 14, "bold"), bg="white", fg="red", anchor='w')
    b = Button(error_frame, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=admin_com)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def adm_nuke():
    faf()
    nu = Frame(r, bg="white")
    nu.grid(padx=20, pady=20, sticky="nsew")

    u = Label(nu, text='Enter the NUKE passcode:', font=("Arial", 14), bg="white", fg="black", anchor='w')
    s = Entry(nu, width=15, font=("Arial", 14), show='*')
    huu = BooleanVar()
    o=Checkbutton(nu,text='show passcode',variable=huu,command=lambda:toggle_password(s,huu))
    b = Button(nu, text='Submit', padx=40, pady=15, fg='white', bg='#FF0000', font=("Arial", 14, "bold"),
               command=lambda: validate_nuke_passcode(s.get(), nu))
    b7=Button(nu,text='Back',padx=40,pady=15,fg='white',bg='#6d7985',command=admin_success)
    b7.grid(row=4,column=0)
    u.grid(row=0, column=0, pady=10, sticky="w")
    s.grid(row=1, column=0, pady=10, sticky="ew")
    b.grid(row=2, column=0, pady=20, sticky="ew")
    o.grid(row=3,column=0)

def validate_nuke_passcode(passcode, frame):
    if passcode == '9846820774':
        frame.grid_forget()
        nuke_confirmation()
    else:
        frame.grid_forget()
        show_incorrect_passcode()


def nuke_confirmation():
    faf()
    ip = Frame(r, bg="white")
    ip.grid(padx=20, pady=20, sticky="nsew")

    lo = Label(ip, text='Are you sure you want to nuke?', font=("Arial", 16, "bold"), bg="white", fg="red", anchor='w')
    b1 = Button(ip, text='Yes', padx=40, pady=15, fg='white', bg='#FF0000', font=("Arial", 14, "bold"),
                command=nuke_final)
    b2 = Button(ip, text='No', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                command=admin_success)

    lo.grid(row=0, column=0, pady=10, sticky="w")
    b1.grid(row=1, column=0, pady=10, sticky="ew")
    b2.grid(row=2, column=0, pady=10, sticky="ew")


def nuke_final():
    try:
        cur.execute('DROP TABLE IF EXISTS properties, agent, customer')
        d.commit()
        show_nuke_success()
    except Exception:
        show_nuke_error()


def show_nuke_success():
    faf()
    jo = Frame(r, bg="white")
    jo.grid(padx=20, pady=20, sticky="nsew")

    er = Label(jo, text='Successfully Nuked!', font=("Arial", 16, "bold"), bg="white", fg="red", anchor='w')
    err = Button(jo, text='OK', padx=40, pady=15, fg='white', bg='#34A853', font=("Arial", 14, "bold"),
                 command=admin_success)

    er.grid(row=0, column=0, pady=20, sticky="w")
    err.grid(row=1, column=0, pady=10, sticky="ew")


def show_nuke_error():
    faf()
    oi = Frame(r, bg="white")
    oi.grid(padx=20, pady=20, sticky="nsew")

    l = Label(oi, text='NUKE failed or tables do not exist', font=("Arial", 14, "bold"), bg="white", fg="red",
              anchor='w')
    b = Button(oi, text='OK', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=admin_success)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")


def show_incorrect_passcode():
    faf()
    error_frame = Frame(r, bg="white")
    error_frame.grid(padx=20, pady=20, sticky="nsew")

    l = Label(error_frame, text='NUKE passcode is incorrect', font=("Arial", 14, "bold"), bg="white", fg="red",
              anchor='w')
    b = Button(error_frame, text='Try Again', padx=40, pady=15, fg='white', bg='#DB4437', font=("Arial", 14, "bold"),
               command=adm_nuke)

    l.grid(row=0, column=0, pady=20, sticky="w")
    b.grid(row=1, column=0, pady=10, sticky="ew")
if r.destroy:
    print('mission successful')

# start the application
firstfunction()
r.mainloop()
