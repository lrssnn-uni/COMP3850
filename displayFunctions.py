from databaseFunctions import *

def printLabelsAndAllRows(rows, desc):
    for k in desc:
        print(k[0], end='\t')

    print('\n--------------------------------------------------------------------------------')

    for row in rows:
        for k in desc:
            print(row[k[0]], end='\t')
        print()


def displayProgramList(c):
   rows = GetPrograms(c)
   printLabelsAndAllRows(rows, c.description)
   return

def displayCourseList(c):
   rows = GetCourses(c)
   printLabelsAndAllRows(rows, c.description)
   return

def displayCoursesInProgram(c, programID):
   rows = GetCoursesInProgram(c, programID)
   printLabelsAndAllRows(rows, c.description)
   return

def displayCoursePrecedents(c, courseID):
   rows = GetCoursePrecedents(c, courseID) 
   printLabelsAndAllRows(rows, c.description)
   return