#create a sqlite3 database and table

#import the sqlite3 libraru
import sqlite3

#create a new database if the database doesn't already exist
conn = sqlite3.connect("webapp.db")

#get a cursor object used to execute SQL commands

cursor = conn.cursor()

#create a table 
cursor.execute(""" CREATE TABLE users
				(firstname TEXT, lastname TEXT, team TEXT, age TEXT)
				""")
				
#close the database connection 
conn.close()
