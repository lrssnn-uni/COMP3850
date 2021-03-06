import sqlite3
from menu_functions import main_menu

conn = sqlite3.connect('DATABASE.sqlite')
conn.row_factory = sqlite3.Row

c = conn.cursor()

# Main Menu
commit = main_menu(c)

if commit:
    conn.commit()

conn.close()
