import sqlite3
from databaseFunctions import *
from displayFunctions import *
from MenuFunctions import *

conn = sqlite3.connect('C:\\Users\\nikla\\COMP3850\\DATABASE.sqlite')
conn.row_factory = sqlite3.Row

c = conn.cursor()

# Main Menu
commit = MainMenu(c)

if commit:
    conn.commit()

conn.close()