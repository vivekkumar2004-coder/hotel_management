from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import mysql.connector
import random

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550")
        
        # Variables
        self.var_Customerid = StringVar()
        x = random.randint(1000, 9999)
        self.var_Customerid.set(str(x))
        
        self.var_Customername = StringVar()
        self.var_mothername = StringVar()
        self.var_fathername = StringVar()
        self.var_gender = StringVar()
        self.var_city = StringVar()
        self.var_mobilenumber = StringVar()
        self.var_state = StringVar()
        self.var_emailid = StringVar()

        # Title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 40, "bold"), bg="black", fg="red", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # img2 = Image.open("C:\\Users\\HP\\Desktop\\p4.png")
        # img2 = img2.resize((100, 40), Image.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        # lblimg2.place(x=5, y=2, width=100, height=40)
        
        # Label Frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("Arial Black", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        lbs_cust_ref = Label(labelframeleft, text="Customer ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbs_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = Entry(labelframeleft, textvariable=self.var_Customerid, width=29, font=("times new roman", 13, "bold"))
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, text="Customer Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = Entry(labelframeleft, textvariable=self.var_Customername, width=29, font=("times new roman", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Mother's Name
        lblmname = Label(labelframeleft, text="Mother's Name:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = Entry(labelframeleft, textvariable=self.var_mothername, width=29, font=("times new roman", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # Father's Name
        lblfname = Label(labelframeleft, text="Father's Name:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblfname.grid(row=3, column=0, sticky=W)
        txtfname = Entry(labelframeleft, textvariable=self.var_fathername, width=29, font=("times new roman", 13, "bold"))
        txtfname.grid(row=3, column=1)

        # Mobile Number
        lblmnumber = Label(labelframeleft, text="Mobile Number:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblmnumber.grid(row=4, column=0, sticky=W)
        txtmnumber = Entry(labelframeleft, textvariable=self.var_mobilenumber, width=29, font=("times new roman", 13, "bold"))
        txtmnumber.grid(row=4, column=1)

        # Gender
        lblgender = Label(labelframeleft, text="Gender:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblgender.grid(row=5, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, width=27, state="readonly", font=("times new roman", 13, "bold"))
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=5, column=1)

        # City
        lblcity = Label(labelframeleft, text="City:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblcity.grid(row=6, column=0, sticky=W)
        txtcity = Entry(labelframeleft, textvariable=self.var_city, width=29, font=("times new roman", 13, "bold"))
        txtcity.grid(row=6, column=1)

        # State
        lblstate = Label(labelframeleft, text="State:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblstate.grid(row=7, column=0, sticky=W)
        txtstate = Entry(labelframeleft, textvariable=self.var_state, width=29, font=("times new roman", 13, "bold"))
        txtstate.grid(row=7, column=1)

        # Email ID
        lblemail = Label(labelframeleft, text="Email ID:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lblemail.grid(row=8, column=0, sticky=W)
        txtemail = Entry(labelframeleft, textvariable=self.var_emailid, width=29, font=("times new roman", 13, "bold"))
        txtemail.grid(row=8, column=1)

        # Button Frame
        button_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(button_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(button_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(button_frame, text="Delete", command=self.Delete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(button_frame, text="Reset", command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("Arial Black", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lbsSearchBY = Label(Table_Frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")
        lbsSearchBY.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, width=24, state="readonly", font=("times new roman", 13, "bold"))
        combo_Search["value"] = ("Mobile", "Customer ID")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)
        
        self.txt_search = StringVar()
        txt_search = Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
        txt_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, command=self.search, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("Customer ID", "Customer Name", "Mother's Name", "Father's Name", "Gender", "City", "Mobile Number", "State", "Email ID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Customer ID", text="Customer ID")
        self.Cust_Details_Table.heading("Customer Name", text="Customer Name")
        self.Cust_Details_Table.heading("Mother's Name", text="Mother's Name")
        self.Cust_Details_Table.heading("Father's Name", text="Father's Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("City", text="City")
        self.Cust_Details_Table.heading("Mobile Number", text="Mobile Number")
        self.Cust_Details_Table.heading("State", text="State")
        self.Cust_Details_Table.heading("Email ID", text="Email ID")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("Customer ID", width=100)
        self.Cust_Details_Table.column("Customer Name", width=100)
        self.Cust_Details_Table.column("Mother's Name", width=100)
        self.Cust_Details_Table.column("Father's Name", width=100)
        self.Cust_Details_Table.column("Gender", width=100)
        self.Cust_Details_Table.column("City", width=100)
        self.Cust_Details_Table.column("Mobile Number", width=100)
        self.Cust_Details_Table.column("State", width=100)
        self.Cust_Details_Table.column("Email ID", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_Customerid.get() == "" or self.var_mobilenumber.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="pandey@123", database="management",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_Customerid.get(),
                    self.var_Customername.get(),
                    self.var_mothername.get(),
                    self.var_fathername.get(),
                    self.var_gender.get(),
                    self.var_city.get(),
                    self.var_mobilenumber.get(),
                    self.var_state.get(),
                    self.var_emailid.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pandey@123", database="management",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_Customerid.set(row[0])
        self.var_Customername.set(row[1])
        self.var_mothername.set(row[2])
        self.var_fathername.set(row[3])
        self.var_gender.set(row[4])
        self.var_city.set(row[5])
        self.var_mobilenumber.set(row[6])
        self.var_state.set(row[7])
        self.var_emailid.set(row[8])

    def update(self):
        if self.var_Customerid.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="pandey@123", database="management",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Customername=%s, Mothername=%s, Fathername=%s, Gender=%s, City=%s, mobilenumber=%s, state=%s, emailid=%s where Customerid=%s", (
                self.var_Customername.get(),
                self.var_mothername.get(),
                self.var_fathername.get(),
                self.var_gender.get(),
                self.var_city.get(),
                self.var_mobilenumber.get(),
                self.var_state.get(),
                self.var_emailid.get(),
                self.var_Customerid.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)

    def Delete(self):
        Delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if Delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="pandey@123", database="management",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query = "delete from customer where Customerid=%s"
            value = (self.var_Customerid.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            if not Delete:
                return

    def reset(self):
        self.var_Customerid.set("")
        self.var_Customername.set("")
        self.var_mothername.set("")
        self.var_fathername.set("")
        self.var_gender.set("")
        self.var_city.set("")
        self.var_mobilenumber.set("")
        self.var_state.set("")
        self.var_emailid.set("")
        x = random.randint(1000, 9999)
        self.var_Customerid.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pandey@123", database="management",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()

        search_by = self.search_var.get().replace(" ", "").lower()
        search_txt = self.txt_search.get()
        query = f"select * from customer where {search_by} LIKE '%{search_txt}%'"
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()
