from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector

class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550")

        # Variables
        self.var_Customer_Contact = StringVar()
        self.var_Check_In_Date = StringVar()
        self.var_Check_Out = StringVar()
        self.var_Available_Room = StringVar()
        self.var_Room_Type = StringVar()
        self.var_Meal = StringVar()
        self.var_Number_Of_Days = StringVar()
        self.var_Total_Cost = StringVar()

        # Title Label
        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 40, "bold"), bg="black", fg="red", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # # Image
        # img2 = Image.open("C:\\Users\\HP\\Desktop\\p4.png")  # Replace with correct path
        # img2 = img2.resize((100, 40), Image.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        # lblimg2.place(x=5, y=2, width=100, height=40)

        # Label Frame Left
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("Arial Black", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = Entry(labelframeleft, textvariable=self.var_Customer_Contact, width=20, font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        btnFetchData = Button(labelframeleft, command=self.fetch_contact, text="Fetch Data", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnFetchData.grid(row=0, column=2, padx=10)

        # Check In Date
        lbl_check_in_date = Label(labelframeleft, text="Check In Date:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_check_in_date.grid(row=1, column=0, sticky=W)

        txt_check_in_date = Entry(labelframeleft, textvariable=self.var_Check_In_Date, width=29, font=("times new roman", 13, "bold"))
        txt_check_in_date.grid(row=1, column=1)

        # Check Out
        lbl_check_out = Label(labelframeleft, text="Check Out:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lbl_check_out.grid(row=2, column=0, sticky=W)

        txt_check_out = Entry(labelframeleft, textvariable=self.var_Check_Out, width=29, font=("times new roman", 13, "bold"))
        txt_check_out.grid(row=2, column=1)

        # Available Room
        lbl_available_room = Label(labelframeleft, text="Available Room:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lbl_available_room.grid(row=3, column=0, sticky=W)

        txt_available_room = Entry(labelframeleft, textvariable=self.var_Available_Room, width=29, font=("times new roman", 13, "bold"))
        txt_available_room.grid(row=3, column=1)

        # Room Type
        label_room_type = Label(labelframeleft, text="Room Type", padx=2, pady=6, font=("times new roman", 12, "bold"))
        label_room_type.grid(row=4, column=0, sticky=W)

        combo_room_type = ttk.Combobox(labelframeleft, textvariable=self.var_Room_Type, width=27, state="readonly", font=("times new roman", 12, "bold"))
        combo_room_type["value"] = ("Single", "Double", "Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(labelframeleft, text="Meal:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lbl_meal.grid(row=5, column=0, sticky=W)

        txt_meal = ttk.Entry(labelframeleft, textvariable=self.var_Meal, font=("times new roman", 12, "bold"), width=29)
        txt_meal.grid(row=5, column=1)

        # Number of Days
        lbl_no_of_days = Label(labelframeleft, text="Number Of Days:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lbl_no_of_days.grid(row=6, column=0, sticky=W)

        txt_no_of_days = Entry(labelframeleft, textvariable=self.var_Number_Of_Days, width=29, font=("times new roman", 13, "bold"))
        txt_no_of_days.grid(row=6, column=1)

        # Total Cost
        lbl_total_cost = Label(labelframeleft, text="Total Cost:", padx=2, pady=6, font=("times new roman", 12, "bold"))
        lbl_total_cost.grid(row=7, column=0, sticky=W)

        txt_total_cost = Entry(labelframeleft, textvariable=self.var_Total_Cost, width=29, font=("times new roman", 13, "bold"))
        txt_total_cost.grid(row=7, column=1)

        # Buttons
        button_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        button_frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(button_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(button_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(button_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(button_frame, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_reset.grid(row=0, column=3, padx=1)

        # Right Side Image
        # img3 = Image.open("C:\\Users\\HP\\Desktop\\bed.png")  # Replace with correct path
        # img3 = img3.resize((520, 200), Image.LANCZOS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)

        # lblimg3 = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        # lblimg3.place(x=760, y=55, width=520, height=200)

        # Table Frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("Arial Black", 12, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        # Search By
        lbl_search_by = Label(table_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")
        lbl_search_by.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, width=24, state="readonly", font=("times new roman", 13, "bold"))
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txt_search = Entry(table_frame, textvariable=self.txt_search, width=24, font=("times new roman", 13, "bold"))
        txt_search.grid(row=0, column=2, padx=2)

        btn_search = Button(table_frame, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(table_frame, text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_show_all.grid(row=0, column=4, padx=1)

        # Details Table
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_table, column=("Customer_Contact", "Check_In_Date", "Check_Out", "Available_Room", "Room_Type", "Meal", "Number_Of_Days", "Total_Cost"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("Customer_Contact", text="Customer Contact")
        self.room_Table.heading("Check_In_Date", text="Check In Date")
        self.room_Table.heading("Check_Out", text="Check Out")
        self.room_Table.heading("Available_Room", text="Available Room")
        self.room_Table.heading("Room_Type", text="Room Type")
        self.room_Table.heading("Meal", text="Meal")
        self.room_Table.heading("Number_Of_Days", text="Number of Days")
        self.room_Table.heading("Total_Cost", text="Total Cost")

        self.room_Table["show"] = "headings"

        self.room_Table.column("Customer_Contact", width=100)
        self.room_Table.column("Check_In_Date", width=100)
        self.room_Table.column("Check_Out", width=100)
        self.room_Table.column("Available_Room", width=100)
        self.room_Table.column("Room_Type", width=100)
        self.room_Table.column("Meal", width=100)
        self.room_Table.column("Number_Of_Days", width=100)
        self.room_Table.column("Total_Cost", width=100)

        self.room_Table.pack(fill=BOTH, expand=1)

    def fetch_contact(self):
        if self.var_Customer_Contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="record")
                my_cursor = conn.cursor()
                query = "select CustomerName from customer where mobilenumber=%s"
                value = (self.var_Customer_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "No record found for this number", parent=self.root)
                else:
                    # Example of displaying fetched data
                    messagebox.showinfo("Success", f"Customer Name: {row[0]}", parent=self.root)

                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)

    def add_data(self):
        if self.var_Customer_Contact.get() == "" or self.var_Check_In_Date.get() == "" or self.var_Check_Out.get() == "" or self.var_Available_Room.get() == "" or self.var_Room_Type.get() == "" or self.var_Meal.get() == "" or self.var_Number_Of_Days.get() == "" or self.var_Total_Cost.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="record")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_Customer_Contact.get(),
                    self.var_Check_In_Date.get(),
                    self.var_Check_Out.get(),
                    self.var_Available_Room.get(),
                    self.var_Room_Type.get(),
                    self.var_Meal.get(),
                    self.var_Number_Of_Days.get(),
                    self.var_Total_Cost.get()
                ))
                conn.commit()
                self.fetch_data()  # Call function to update table
                conn.close()
                messagebox.showinfo("Success", "Data added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error adding data: {str(e)}", parent=self.root)

    def fetch_data(self):
        # Implement this function to fetch data from the database and populate the Treeview
        pass  # Replace with actual implementation

# # Testing the class
# if __name__ == "__main__":
#     root = Tk()
#     obj = roombooking(root)
#     root.mainloop()
