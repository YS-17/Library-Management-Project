# Imports
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as sqlcon
from mysql.connector import Error

My_Sql_Password = 'yuvraj' # Replace with MySQL password

# Function To Create A Connection To MySQL Server
def create_connection():
    try:
        connection = sqlcon.connect(
            host='localhost',
            user='root',
            password = My_Sql_Password  
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
# Function To Execute SQL Queries
def execute_query(connection, query, values=None):
    try:
        cursor = connection.cursor()
        if values:
            cursor.executemany(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")

# Create Library_Management Database
create_db_query = "CREATE DATABASE IF NOT EXISTS Library_Management"

create_user_table_query = """
CREATE TABLE IF NOT EXISTS User ( 
    ID INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20) NOT NULL, 
    Gender CHAR(1) NOT NULL, 
    Date_Of_Birth DATE, 
    Phone_No CHAR(10), 
    Email VARCHAR(50), 
    Password CHAR(16) NOT NULL
)
"""

create_librarian_table_query = """
CREATE TABLE IF NOT EXISTS Librarian ( 
    ID INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20) NOT NULL, 
    Gender CHAR(1) NOT NULL, 
    Date_Of_Birth DATE, 
    Phone_No CHAR(10), 
    Email VARCHAR(50), 
    Password CHAR(16) NOT NULL
)
"""

create_books_table_query = """
CREATE TABLE IF NOT EXISTS Books (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(50) NOT NULL,
    Author VARCHAR(20) NOT NULL,
    Genre VARCHAR(20) NOT NULL,
    Copies INT(3) NOT NULL
)
"""

create_books_issued_table_query = """
CREATE TABLE IF NOT EXISTS Books_Issued (
    Issued_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT(3) NOT NULL,
    User_Name VARCHAR(20) NOT NULL,
    Book_ID INT(3) NOT NULL,
    Book_Name VARCHAR(50) NOT NULL,
    Issue_Date DATE,
    Return_Date DATE
)
"""

# Insert multiple values into User table
insert_user_values = [
    ('Yuvraj', 'M', '2007-09-17', '9876543210', 'bcm.yuvraj@gmail.com', 'y'),
    ('Dhaval', 'M', '2007-10-18', '9876543211', 'bcm.dhaval@gmail.com', 'd'),
    ('Raghav', 'M', '2006-11-06', '9876543212', 'bcm.raghav@gmail.com', 'r'),
    ('Ashwinder', 'M', '2007-12-20', '9876543213', 'bcm.ashwinder@gmail.com', 'a'),
    ('Gurtej', 'M', '2007-01-21', '9876543214', 'bcm.gurtej@gmail.com', 'g'),
    # Can Add More Values
]

insert_user_query = """
INSERT INTO User (Name, Gender, Date_Of_Birth, Phone_No, Email, Password)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Insert multiple values into Librarian table
insert_librarian_values = [
    ('Yuvraj', 'M', '2007-09-17', '9876543210', 'bcm.yuvraj@gmail.com', 'y'),
    ('Dhaval', 'M', '2007-10-18', '9876543211', 'bcm.dhaval@gmail.com', 'd'),
    ('Ashwinder', 'M', '2007-12-20', '9876543213', 'bcm.ashwinder@gmail.com', 'a'),
    # Can Add More Values
]

insert_librarian_query = """
INSERT INTO Librarian (Name, Gender, Date_Of_Birth, Phone_No, Email, Password)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Insert multiple values into Books table
insert_books_values = [
    ('Captian Underpants','Dav Pilkey','Comedy',1),
    ("Harry Potter", "J.K. Rowling", "Fantasy", 3),
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", 2),
    # Can Add More Values
]

insert_books_query = """
INSERT INTO Books (Title, Author, Genre, Copies)
VALUES (%s, %s, %s, %s)
"""

# Insert multiple values into Books_Issued table
insert_books_issued_values = [
    (1,'Yuvraj',1,'Captian Underpants','2008.03.03','2021.10.14'),
    (2, 'Dhaval', 2, 'Harry Potter', '2022-01-22', '2022-02-20'),
    (3, 'Raghav', 3, 'To Kill a Mockingbird', '2020-01-22', '2024-02-20'),
    # Can Add More Values
]

insert_books_issued_query = """
INSERT INTO Books_Issued (User_ID, User_Name, Book_ID, Book_Name, Issue_Date, Return_Date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Main script
connection = create_connection()

if connection:
    try:
        # Create the Library_Management database
        execute_query(connection, create_db_query)

        # Use the Library_Management database
        connection.database = "Library_Management"

        # Create The User Table
        execute_query(connection, create_user_table_query)

        # Create the Librarian table
        execute_query(connection, create_librarian_table_query)

        # Create the Books table
        execute_query(connection, create_books_table_query)

        # Create the Books_Issued table
        execute_query(connection, create_books_issued_table_query)

        # Insert values into the user table
        execute_query(connection, insert_user_query, insert_user_values)

        # Insert values into the librarian table
        execute_query(connection, insert_librarian_query, insert_librarian_values)

        # Insert values into the Books table
        execute_query(connection, insert_books_query, insert_books_values)

        # Insert values into the Books_Issued table
        execute_query(connection, insert_books_issued_query, insert_books_issued_values)

    finally:
        # Close the database connection
        connection.close()

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": My_Sql_Password,
    "database": "Library_Management"
}

# Function To Handle Database Connection
def connect_db():
    try:
        mydb = sqlcon.connect(**DB_CONFIG)
        return mydb
    except sqlcon.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None

# Function To Execute A Query And Fetch Results
def execute_query(query, values=None):
    with connect_db() as mydb:
        mycursor = mydb.cursor()
        try:
            mycursor.execute(query, values)
            results = mycursor.fetchall()
            return results
        except sqlcon.Error as e:
            messagebox.showerror("Database Error", f"Error executing query: {e}")
            return None

# Function To Execute An Update Query
def execute_update(query, values=None):
    with connect_db() as mydb:
        mycursor = mydb.cursor()
        try:
            mycursor.execute(query, values)
            mydb.commit()
        except sqlcon.Error as e:
            messagebox.showerror("Database Error", f"Error updating database: {e}")

# Function To Show A Message
def show_message(title, message):
    messagebox.showinfo(title, message)

# Function To Issue A Book
def issue_book_action(user_id, book_id):
    user_query = "SELECT * FROM User WHERE ID = %s"
    book_query = "SELECT * FROM Books WHERE ID = %s"

    user_result = execute_query(user_query, (user_id,))
    book_result = execute_query(book_query, (book_id,))

    if user_result and book_result:
        available_copies = book_result[0][4]

        if available_copies > 0:
            update_book_query = "UPDATE Books SET Copies = Copies - 1 WHERE ID = %s"
            execute_update(update_book_query, (book_id,))

            insert_issued_query = "INSERT INTO Books_Issued (User_ID, User_Name, Book_ID, Book_Name, Issue_Date) VALUES (%s, %s, %s, %s, CURRENT_DATE)"
            insert_issued_values = (user_id, user_result[0][1], book_id, book_result[0][1])
            execute_update(insert_issued_query, insert_issued_values)

            show_message("Success", "Book issued successfully!")
        else:
            show_message("Error", "No available copies of the book.")
    else:
        show_message("Error", "User or book not found.")

# Function To Return A Book
def return_book_action(user_id, book_id):
    user_query = "SELECT * FROM User WHERE ID = %s"
    book_query = "SELECT * FROM Books WHERE ID = %s"

    user_result = execute_query(user_query, (user_id,))
    book_result = execute_query(book_query, (book_id,))

    if user_result and book_result:
        issued_query = "SELECT * FROM Books_Issued WHERE User_ID = %s AND Book_ID = %s"
        issued_values = (user_id, book_id)
        issued_result = execute_query(issued_query, issued_values)

        if issued_result:
            update_book_query = "UPDATE Books SET Copies = Copies + 1 WHERE ID = %s"
            execute_update(update_book_query, (book_id,))

            delete_issued_query = "DELETE FROM Books_Issued WHERE User_ID = %s AND Book_ID = %s"
            delete_issued_values = (user_id, book_id)
            execute_update(delete_issued_query, delete_issued_values)

            show_message("Success", "Book returned successfully!")
        else:
            show_message("Error", "The user has not issued this book.")
    else:
        show_message("Error", "User or book not found.")

# Function To Search For Books
def search_books(title):
    sql = "SELECT * FROM Books WHERE Title LIKE %s"
    values = ("%" + title + "%",)

    results = execute_query(sql, values)

    if results:
        for book in results:
            print(book)
    else:
        show_message("Info", "No books found matching the search criteria.")

# Function To Update The Result Display
def update_result_display(listbox, results):
    listbox.delete(0, tk.END)  # Clear Previous Results

    if results:
        for book in results:
            listbox.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Copies: {book[4]}")
    else:
        listbox.insert(tk.END, "No books found matching the search criteria.")

# Function To Handle The Back Button
def back(window):
    window.destroy()

# Function To Insert Values To Database
def insert(Table,Name,Gender,Year,Month,Day,Phone_No,Email,Password,Page):
    DOB = (f"{Year}-{Month}-{Day}")
    if Name and Gender and Year and Month and Day and Phone_No and Email and Password:
        try:
            mydb = connect_db()
            mycursor = mydb.cursor()

            if Table == 'User' :
                sql = "INSERT INTO User (Name, Gender, Date_Of_Birth, Phone_No, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)"

            elif Table == 'Librarian' :
                sql = "INSERT INTO Librarian (Name, Gender, Date_Of_Birth, Phone_No, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)"

            val = (Name, Gender, DOB, Phone_No, Email, Password)

            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Data Added Successfully")
        except sqlcon.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            mycursor.close()
            mydb.close()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")
    back(Page)

# GUI For Issuing A Book
def issue_book():
    issue_book_window = tk.Toplevel()  # Use Toplevel instead of Tk to create a new window
    issue_book_window.title("Issue Book")
    issue_book_window.attributes('-fullscreen', True)

    labels = ["User ID", "Book ID"]
    entries = [tk.Entry(issue_book_window, width=25, bd=4, bg='orange') for _ in range(len(labels))]

    for label, entry in zip(labels, entries):
        tk.Label(issue_book_window, text=label + ":", font='Papyrus 14 bold', fg='White', bg='Black').pack(pady=10)
        entry.pack(pady=10)

    tk.Button(issue_book_window, text="Issue Book", font='Papyrus 14 bold', fg='White', bg='Black', width=10,
              padx=0.5, borderwidth=0, command=lambda: issue_book_action(entries[0].get(), entries[1].get())).pack(pady=10)

    tk.Button(issue_book_window, text="Back", font='Papyrus 14 bold', fg='White', bg='Black', width=8,
              padx=0.5, borderwidth=0, command=lambda: back(issue_book_window)).pack(pady=10)

# GUI For Returning A Book
def return_book():
    return_book_window = tk.Toplevel()  # Use Toplevel instead of Tk to create a new window
    return_book_window.title("Return Book")
    return_book_window.attributes('-fullscreen', True)

    labels = ["User ID", "Book ID"]
    entries = [tk.Entry(return_book_window, width=25, bd=4, bg='orange') for _ in range(len(labels))]

    for label, entry in zip(labels, entries):
        tk.Label(return_book_window, text=label + ":", font='Papyrus 14 bold', fg='White', bg='Black').pack(pady=10)
        entry.pack(pady=10)

    tk.Button(return_book_window, text="Return Book", font='Papyrus 14 bold', fg='White', bg='Black', width=10,
              padx=0.5, borderwidth=0, command=lambda: return_book_action(entries[0].get(), entries[1].get())).pack(pady=10)

    tk.Button(return_book_window, text="Back", font='Papyrus 14 bold', fg='White', bg='Black', width=8,
              padx=0.5, borderwidth=0, command=lambda: back(return_book_window)).pack(pady=10)

# GUI For Searching Books
def search_book():
    def search_books(title):
        sql = "SELECT * FROM Books WHERE Title LIKE %s"
        values = ("%" + title + "%",)
        results = execute_query(sql, values)
        update_result_display(result_listbox, results)

    search_book_window = tk.Toplevel()  # Use Toplevel instead of Tk to create a new window
    search_book_window.title("Search Book")
    search_book_window.attributes('-fullscreen', True)  # Open in full screen

    label_search = tk.Label(search_book_window, text="Search Book:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_search.pack(pady=10)

    entry_search = tk.Entry(search_book_window, width=26, bd=8, bg='orange')
    entry_search.pack(pady=10)

    result_listbox = tk.Listbox(search_book_window, width=100, height=20, bg='orange', font='Papyrus 12', selectbackground='Black')
    result_listbox.pack(pady=10)

    tk.Button(search_book_window, text="Search Book", font='Papyrus 14 bold', fg='White', bg='Black', width=10,
              padx=0.5, borderwidth=0, command=lambda: search_books(entry_search.get())).pack(pady=10)

    tk.Button(search_book_window, text="Back", font='Papyrus 14 bold', fg='White', bg='Black', width=8,
              padx=0.5, borderwidth=0, command=lambda: back(search_book_window)).pack(pady=10)

    search_book_window.mainloop()

# GUI For Login
def Login():
    def validate_login(Table ,Name, ID, Password, Page):
        if Name and ID and Password:
            try:
                mydb = connect_db()
                mycursor = mydb.cursor()

                if Table == 'User' :
                    sql = "SELECT * FROM User WHERE Name = %s AND ID = %s AND Password = %s"
                
                elif Table == 'Librarian' :
                    sql = "SELECT * FROM Librarian WHERE Name = %s AND ID = %s AND Password = %s"
                
                val = (Name, ID, Password)

                mycursor.execute(sql, val)
                result = mycursor.fetchone()

                if result:
                    messagebox.showinfo("Success", "Login successful")
                    if Table == 'User' :
                        pass
                    elif Table == 'Librarian' :
                        pass
                                                                 
                else:
                    messagebox.showerror("Error", "Invalid credentials")
            except sqlcon.Error as e:
                messagebox.showerror("Error", f"Database error: {e}")
            finally:
                mycursor.close()
                mydb.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
        back(Page)

    login_page = tk.Toplevel()  # Use Toplevel instead of Tk to create a new window
    login_page.title("Search Book")
    login_page.attributes('-fullscreen', True)  # Open in full screen

    label_Table = tk.Label(login_page, text="Login As :", font='Papyrus 16 bold', fg='White', bg='Black')
    label_Table.pack(pady=10)
    Table_Var = tk.StringVar(login_page)
    Table_options = ("User", "Librarian")
    
    Table_spinbox = tk.Spinbox(login_page, textvariable=Table_Var, values=Table_options, width=26, bd=8, bg='orange')
    Table_spinbox.pack(pady=10)

    label_Name = tk.Label(login_page, text="Name :", font='Papyrus 16 bold', fg='White', bg='Black')
    label_Name.pack(pady=10)
    
    entry_Name = tk.Entry(login_page, width=26, bd=8, bg='orange')
    entry_Name.pack(pady=10)

    label_ID = tk.Label(login_page, text="ID :", font='Papyrus 16 bold', fg='White', bg='Black')
    label_ID.pack(pady=10)
    
    entry_ID = tk.Entry(login_page, width=26, bd=8, bg='orange')
    entry_ID.pack(pady=10)

    label_Password = tk.Label(login_page, text="Password :", font='Papyrus 16 bold', fg='White', bg='Black')
    label_Password.pack(pady=10)
    
    entry_Password = tk.Entry(login_page, width=26, bd=8, bg='orange', show="*")
    entry_Password.pack(pady=10)

    tk.Button(login_page, text="Login", font='Papyrus 14 bold', fg='White', bg='Black', width=10,
              padx=0.5, borderwidth=0, command=lambda: validate_login(Table_Var.get(), entry_Name.get(), entry_ID.get()
                                                                      , entry_Password.get(), login_page)).pack(pady=10)

    tk.Button(login_page, text="Back", font='Papyrus 14 bold', fg='White', bg='Black', width=8,
              padx=0.5, borderwidth=0, command=lambda: back(login_page)).pack(pady=10)
    
    login_page.mainloop()
    
# GUI For SignUp
def SignUp():
    SignUp_page = tk.Toplevel()  # Use Toplevel instead of Tk to create a new window
    SignUp_page.title("User SignUp")
    SignUp_page.attributes('-fullscreen', True)  # Open in full screen

    # Name
    label_name = tk.Label(SignUp_page, text="Name:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_name.pack(pady=10)
    entry_name = tk.Entry(SignUp_page, width=26, bd=8, bg='orange')
    entry_name.pack(pady=10)

    # Gender
    label_gender = tk.Label(SignUp_page, text="Gender:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_gender.pack(pady=10)

    gender_var = tk.StringVar(SignUp_page)
    gender_options = ("M", "F", "O")  # Gender options
    gender_spinbox = tk.Spinbox(SignUp_page, textvariable=gender_var, values=gender_options, width=26, bd=8, bg='orange')
    gender_spinbox.pack(pady=10)

    # Date Of Birth
    label_dob = tk.Label(SignUp_page, text="Date Of Birth (Year-Month-Day):", font='Papyrus 16 bold', fg='White', bg='Black')
    label_dob.pack(pady=10)

    dob_frame = tk.Frame(SignUp_page)
    dob_frame.pack(pady=10)

    dob_year = tk.Spinbox(dob_frame, from_=1900, to=2100, width=26, bd=8, bg='orange')
    dob_month = tk.Spinbox(dob_frame, from_=1, to=12, width=23, bd=8, bg='orange')
    dob_day = tk.Spinbox(dob_frame, from_=1, to=31, width=23, bd=8, bg='orange')

    dob_year.pack(side=tk.LEFT, padx=5,pady=10)
    tk.Label(dob_frame, text='-', font=("Arial", 12)).pack(side=tk.LEFT,pady=10)
    dob_month.pack(side=tk.LEFT, padx=5,pady=10)
    tk.Label(dob_frame, text='-', font=("Arial", 12)).pack(side=tk.LEFT,pady=10)
    dob_day.pack(side=tk.LEFT, padx=5,pady=10)

    # Phone No.
    label_phone = tk.Label(SignUp_page, text="Phone No.:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_phone.pack(pady=10)
    
    entry_phone = tk.Entry(SignUp_page, width=26, bd=8, bg='orange')
    entry_phone.pack(pady=10)

    # Email
    label_email = tk.Label(SignUp_page, text="Email:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_email.pack(pady=10)
    
    entry_email = tk.Entry(SignUp_page, width=26, bd=8, bg='orange')
    entry_email.pack(pady=10)

    # Password
    label_password = tk.Label(SignUp_page, text="Password:", font='Papyrus 16 bold', fg='White', bg='Black')
    label_password.pack(pady=10)

    entry_password = tk.Entry(SignUp_page, width=26, bd=8, bg='orange')
    entry_password.pack(pady=10)

    # Add Button
    tk.Button(SignUp_page, text="Add User", font='Papyrus 14 bold', fg='White', bg='Black', width=10, padx=0.5, borderwidth=0,
              command=lambda: insert("User", entry_name.get(), gender_var.get() , dob_year.get(), dob_month.get(), dob_day.get(),
                                      entry_phone.get(), entry_email.get(), entry_password.get(),SignUp_page)).pack(pady=10)

    tk.Button(SignUp_page, text="Back", font='Papyrus 14 bold', fg='White', bg='Black', width=8,
              padx=0.5, borderwidth=0, command=lambda: back(SignUp_page)).pack(pady=10)

    SignUp_page.mainloop()

# GUI For Main Window
def Main_Window():
    Main_Window = tk.Tk()
    Main_Window.title("Main Window")
    Main_Window.state('zoomed')
    ttk.Label(text="Welcome to Library Management System", font=('Helvetica', 18, 'bold')).pack(pady=20)

    button_texts = ["Issue Book", "Return Book", "Search Book"]
    button_commands = [issue_book, return_book, search_book]

    button_texts_1 = ["SignUp", "Login"]
    button_commands_1 = [SignUp, Login]

    for text, command in zip(button_texts, button_commands):
        tk.Button(Main_Window, text=text, font='Papyrus 22 bold', fg='White', bg='Black', width=19, padx=10,
                  borderwidth=0, command=command).pack(pady=20)
        
    for text_1, command_1 in zip(button_texts_1, button_commands_1):
        tk.Button(Main_Window, text=text_1, font='Papyrus 12 bold', fg='White', bg='Black', width=8, padx=10,
                  borderwidth=0, command=command_1).pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    Main_Window.mainloop()

# Calling The Function For Main Window
Main_Window()
