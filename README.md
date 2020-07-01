COMP3850 - Database Administration Tool

Included Files:
  - DATABASE.sqlite - Base copy of database, fully populated.
  - DATABASE_CREATE.sql - SQL Queries to bootstrap database. (not needed except to reset DATABASE.sqlite)
  - README.md
  - database_functionality.py - Python functions to operate on the database.
  - display_functions.py - Python functions to assist in translating database rows into display
  - main.py - Program wrapper
  - menu_functions.py - Python functions controlling menu flow and display
  - sqlite3.exe - Copy of sqlite3 library to allow direct interaction with database file (for testing/inspection)

Usage:
  Simply clone the repo and run the tool:
    > py main.py
    
  The database can be inspected in the sqlite console (note that our tool will not commit transactions until save and quit).
