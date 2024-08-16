'''
import sqlite3


con = sqlite3.connect("college.db")
print("Database opened successfully")

#con.execute("create table students (UserId VARCHAR PRIMARY KEY NOT NULL, password TEXT NOT NULL)")
con.execute("create table Unanswered(serial_no INT , question TEXT )")
print("Table created successfully")

con.close()

import sqlite3

con = sqlite3.connect("college.db")
print("Database opened successfully")

# You can use INTEGER PRIMARY KEY AUTOINCREMENT to create an auto-incrementing serial number.
con.execute("create table Unanswered(serial_no INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT)")
print("Table created successfully")

con.close()
'''
import sqlite3

con = sqlite3.connect("college.db")
print("Database opened successfully")

con.execute("create table Unanswereds(serial_no INTEGER PRIMARY KEY , question VARCHAR NOT NULL)")
print("Table created successfully")

con.close()