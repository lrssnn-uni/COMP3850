import sqlite3
from databaseFunctions import *

conn = sqlite3.connect('C:\\Users\\nikla\\DatabaseHelper\\DATABASE.sqlite')
conn.row_factory = sqlite3.Row

c = conn.cursor()

""" for row in GetPrograms(c):
  print(row)
print("Adding")
AddProgram(c, "DummyProgram")

for row in GetPrograms(c):
  print(row)

print("Removing")
RemoveProgram(c, "DummyProgram")

for row in GetPrograms(c):
  print(row) """

# for row in GetProgramsInCourse(c, 1):
#   print(row["Course_Code"], ", ", row["directed_group"])

# print('inserting')
# AddCourseToProgram(c, 1, 54, 0)

# for row in GetProgramsInCourse(c, 1):
#   print(row["Course_Code"])

# print('removing')
# RemoveCourseFromProgram(c, 1, 54)

# for row in GetProgramsInCourse(c, 1):
#   print(row["Course_Code"])

# for row in GetCoursesInDirectedGroup(c, 1, 2):
#   print(row["Course_Code"])


for row in GetDirectedGroupsByProgram(c, 1):
  print(row["directed_group"], row["number_required"])
   
AddDirectedGroupToProgram(c, 1, 2, 5)
print("Adding")

for row in GetDirectedGroupsByProgram(c, 1):
  print(row["directed_group"], row["number_required"])
   
RemoveDirectedGroupFromProgram(c, 1, 2)
print("Removing")

for row in GetDirectedGroupsByProgram(c, 1):
  print(row["directed_group"], row["number_required"])