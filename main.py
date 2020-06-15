import sqlite3
from databaseFunctions import *
from displayFunctions import *
from MenuFunctions import *

conn = sqlite3.connect('C:\\Users\\nikla\\DatabaseHelper\\DATABASE.sqlite')
conn.row_factory = sqlite3.Row

c = conn.cursor()

# Main Menu
while True:
    MainMenu(c)