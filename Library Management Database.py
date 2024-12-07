# Imports
from tkinter import messagebox
import mysql.connector as sqlcon
from mysql.connector import Error

My_Sql_Password = 'yuvraj' # Replace with MySQL password
Do_You_Want_To_Delete_Old_Database = 'yes' # Type 'yes' or 'no'

''' SQL Connection Codes '''

# Function To Create A Connection To MySQL Server
def connect_SQ():
    try:
        connection = sqlcon.connect(host='localhost',user='root',password = My_Sql_Password)
        return connection
    except Error as e:
        if e.errno == 1062:  # MySQL error code for duplicate entry
            print("Duplicate Entry Found")
        else:
            print(f"Error: {e}")
        return None
    
def connect_db():
    try:
        connection = sqlcon.connect(
            host='localhost',
            user='root',
            password = My_Sql_Password,
            database = "Library_Management"
    )
        return connection
    except Error as e:
        if e.errno == 1062:  # MySQL error code for duplicate entry
            print("Duplicate Entry Found")
        else:
            messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None

# Function To Execute SQL Queries
def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.executemany(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        if e.errno == 1062:  # MySQL error code for duplicate entry
            print("Duplicate Entry Found")
        else:
            print(f"Error: {e}")
        
''' SQL Commands '''

# Drop Library_Management Database
if Do_You_Want_To_Delete_Old_Database == 'yes':
    drop_db_query = "DROP DATABASE Library_Management"

# Create Library_Management Database
create_db_query = "CREATE DATABASE IF NOT EXISTS Library_Management"

# Create Books Table
create_books_table_query = """
CREATE TABLE IF NOT EXISTS Book (
    Book_ID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) UNIQUE NOT NULL,
    Genre VARCHAR(20) NOT NULL
)
"""

# Create Book Copies Table
create_book_copies_table_query = """
CREATE TABLE IF NOT EXISTS Book_Copies (
    Book_ID INT PRIMARY KEY,
    No_Of_Copies INT NOT NULL,
    FOREIGN KEY (Book_ID) REFERENCES BOOK(Book_ID)
        ON DELETE CASCADE ON UPDATE CASCADE
)
"""

# Create Book Authors Table
create_book_authors_table_query = """
CREATE TABLE IF NOT EXISTS Book_Authors (
    Book_ID INT NOT NULL,
    Author_Name VARCHAR(255) NOT NULL,
    PRIMARY KEY (Book_ID, Author_Name),
    FOREIGN KEY (Book_ID) REFERENCES BOOK(Book_ID)
        ON DELETE CASCADE ON UPDATE CASCADE
)
"""

# Create Borrower Table
create_borrower_table_query = """
CREATE TABLE IF NOT EXISTS Borrower ( 
    Card_No INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(55) NOT NULL,
    Address TEXT,
    Email VARCHAR(255) UNIQUE ,
    Phone VARCHAR(10) UNIQUE NOT NULL
)
"""

# Create Book Loan Table
create_book_loans_table_query = """
CREATE TABLE IF NOT EXISTS Book_Loans (
    Book_ID INT NOT NULL,
    Card_No INT NOT NULL,
    Date_Out DATE NOT NULL,
    Due_Date DATE,
    PRIMARY KEY (Book_ID, Card_No, Date_Out),
    FOREIGN KEY (Book_ID) REFERENCES BOOK(Book_ID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Card_No) REFERENCES BORROWER(Card_No)
        ON DELETE CASCADE ON UPDATE CASCADE
)
"""

# Create Librarian Table
create_librarian_table_query = """
CREATE TABLE IF NOT EXISTS Librarian ( 
    Librarian_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address TEXT,
    Email VARCHAR(255) UNIQUE ,
    Phone VARCHAR(15) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
)
"""

# Inserting in Book
insert_book_query = """
INSERT INTO Book (Title, Genre)
VALUES (%s, %s)
"""
book_values = [
    ("Naruto", "Manga"),
    ("Jujutsu Kaisen", "Manga"),
    ("Demon Slayer", "Manga"),
    ("Dragon Ball", "Manga"),
    ("Solo Leveling", "Novel"),
    ("Death Note", "Manga"),
    ("Bleach", "Manga")
]

# Inserting in Book Copies
insert_book_copies_query = """
INSERT INTO Book_Copies (Book_ID, No_Of_Copies)
VALUES (%s, %s)
"""
book_copies_values = [
    (1, 15),  # For Book_ID 1 
    (2, 9),
    (3, 7),
    (4, 3),
    (5, 11),
    (6, 13),
    (7, 5)
]

# Inserting in Book Authors
insert_book_authors_query = """
INSERT INTO Book_Authors (Book_ID, Author_Name)
VALUES (%s, %s)
"""
book_authors_values = [
    (1, "Masashi Kishimoto"),
    (2, "Gege Akutami"),
    (3, "Koyoharu Gotouge"),
    (4, "Akira Toriyama"),
    (5, "Chu-Gong"),
    (6, "Tsugumi Ohba"),
    (7, "Tite Kubo")
]

# Inserting in Borrower Table
insert_borrower_query = """
INSERT INTO Borrower (Name, Address, Email, Phone)
VALUES (%s, %s, %s, %s)
"""
borrower_values = [
    ("Palki", "221 Basant St", "Palki@email.com","7973484399"),
    ("Dhaval", "123 Main St", "Dhaval@email.com", "9876543210"),
    ("Raghav", "456 Elm St", "Raghav@email.com", "9876543211")
]

# Inserting in Book Loans
insert_book_loans_query = """
INSERT INTO Book_Loans (Book_ID, Card_No, Date_Out, Due_Date)
VALUES (%s, %s, %s, %s)
"""
book_loans_values = [
    (3, 2, '2024-10-18', '2024-11-01'),  # Dhaval borrowing "Demon Slayer"
    (4, 3, '2024-11-06', '2024-11-20'),   # Raghav borrowing "Dragon Ball"
    # (1, 1, '2025-01-09', '2025-01-23') # Palki borrowing "Naruto"
]

# Inserting in Librarian Table
insert_librarian_query = """
INSERT INTO Librarian (Name, Address, Email, Phone, Password)
VALUES (%s, %s, %s, %s, %s)
"""
librarian_values = [
    ("1", "1 Basi St", "One@email.com", "1234567892", "1"),
    ("Yuvraj", "220 Basant St", "Yuvraj@email.com", "1234567893", "y"),
    ("Ashwinder", "321 Oak St", "Ashwinder@email.com", "1234567894", "a"),
    ("Madhav", "789 Pine St", "Madhav@email.com", "1234567895", "m"),
]

# Main SQL Script
connection = connect_SQ()

if connection:
    try:
        if Do_You_Want_To_Delete_Old_Database == 'yes':
            # Drop the Library_Management database
            execute_query(connection, drop_db_query)

        # Create the Library_Management database
        execute_query(connection, create_db_query)

        # Use the Library_Management database
        connection.database = "Library_Management"

        # Create The Books Table
        execute_query(connection, create_books_table_query)

        # Create the Book_Copies table
        execute_query(connection, create_book_copies_table_query)

        # Create the Book_Copies table
        execute_query(connection, create_book_authors_table_query)

        # Create the Borrower table
        execute_query(connection, create_borrower_table_query)

        # Create the Book_Loans table
        execute_query(connection, create_book_loans_table_query)

        # Create the Librarian table
        execute_query(connection, create_librarian_table_query)     

        # Insert book data
        execute_query(connection, insert_book_query, book_values)

        # Insert book copies data
        execute_query(connection, insert_book_copies_query, book_copies_values)

        # Insert book authors data
        execute_query(connection, insert_book_authors_query, book_authors_values)

        # Insert borrower data
        execute_query(connection, insert_borrower_query, borrower_values)

        # Insert book loans data
        execute_query(connection, insert_book_loans_query, book_loans_values)

        # Insert librarian data
        execute_query(connection, insert_librarian_query, librarian_values)

    finally:
        # Close the connection after the insertions
        connection.close()
