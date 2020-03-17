# Remember to start the MySQL daemon in Windows Services or MySQL notifier
# On Manjaro use "sudo systemctl start mysqld.service"

import os
import MySQLdb

# Get user information
dbName = input("Please enter the name of your databse: ")
username = input("Please enter your mysql username: ")
password = input("Please enter your mysql password: ")

# Create objects
try:
    dbConnector = MySQLdb.connect("localhost", username, password, dbName)
    cursor = dbConnector.cursor()
except:
    print("Error, Unable to connect to database")

# Create the table
#cursor.execute("DROP TABLE IF EXISTS list")
tableCreate = """CREATE TABLE list(\nArtist VARCHAR(20),\nDate VARCHAR(20),\nVenue VARCHAR(20))"""

try:
    cursor.execute(tableCreate)
    dbConnector.commit()
except:
    dbConnector.rollback()

# Add an entry
artist = input("Artist: ")
date = input("Date: ")
venue = input("Venue: ")
entry1 = "INSERT INTO list(Artist, Date, Venue)\nVALUES('" +  artist +"', '" + date + "', '" + venue + "')"
try:
    cursor.execute(entry1)
    dbConnector.commit()
except:
    dbConnector.rollback()

# Remember to close the database
dbConnector.close()
