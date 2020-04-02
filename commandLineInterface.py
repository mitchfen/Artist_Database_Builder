import sqlite3
from sqlite3 import Error
from tabulate import tabulate

###################################################
#   Command line code
#   This code was written for the command line functionality.
#   No longer needed now that the GUI is functional
###################################################

# Main program loop, where user input is accepted
def cmdPromptLoop(connector, cursor):

    keepGoing = True
    while(keepGoing):

        print("1) Print the table")
        print("2) Add a new entry")
        print("3) Remove an entry")
        print("4) Edit an entry")
        print("5) Exit")

        i = int(input("Command: "))
        if i == 1:  printTableToCMD(cursor)
        elif i == 2: addEntryFromCMD(connector)
        elif i == 3: removeEntryFromCMD(connector)
        elif i == 4: editEntryFromCMD(connector)
        elif i == 5: keepGoing = False

# Print the table using tabulate
def printTableToCMD(cursor):
        cursor.execute("SELECT * FROM showTable")
        entries = []
        entries = cursor.fetchall()
        print(tabulate(entries))

def addEntryFromCMD(connector):
    artist = input("Artist: ")
    date = input("Date: ")
    venue = input("Venue: ")

    sql = "INSERT INTO showTable (ID, Artist, Date, Venue)\nValues(NULL, '" + artist + "', '" + date + "', '" + venue + "') "

    connector.execute(sql)
    connector.commit()


# TODO
def removeEntryFromCMD(connector):
   return 

# TODO
def editEntryFromCMD(connector):
    return