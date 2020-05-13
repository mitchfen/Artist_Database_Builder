
# Artist Database Builder

### Overview

I go to a lot of concerts, and was having trouble keeping track of who I have/haven't seen. I need a solution that allows me to select all the artists I have seen at a given venue, year, etc.  

Excel and Excel macros are alright, but  SQLite is better for performing queries.  
SQLite is also more relevant to my future interests and this project was a good opportunity to learn how to build a GUI in Python.

The program has an alternative command line interface and works on Windows 10 and Linux.

### Screens

Main window  
![image1 not found](https://github.com/mitchfen/artist-database/blob/master/screenshots/screen1.png)  

View table screen  
![image2 not found](https://github.com/mitchfen/artist-database/blob/master/screenshots/screen2.png)


### Dependencies

* You need [sqlite3](https://sqlite.org/download.html) on your machine.
* If you are on Linux you may need to install Tkinter manually.
    * `pacman -S python-pmw` on Arch/Manjaro.
    * `apt-get install python-tk` on Debian and its derivatives.
* Tabulate python module: `pip install tabulate`
* You may want a program to view the db file but it is not required. I like [sqliteonline.com](https://sqliteonline.com/) and [SQLiteStudio](https://github.com/pawelsalawa/sqlitestudio/releases).

### Running the program

 Run the commmand `python .\src\main.py`
