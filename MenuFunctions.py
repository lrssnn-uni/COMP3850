from displayFunctions import *
from databaseFunctions import *

def getIntegerChoice(minRange, maxRange):
    valid = False
    while(not valid):
        try:
            i = int(input(f'Choice ({minRange} - {maxRange}): '))
        except ValueError:
            print("Invalid Input: Please input a number")
            valid = False
            continue
        # We have a valid number, check range
        if(i >= minRange and i <= maxRange):
            valid = True
        else:
            print("Invalid Input: Outside range")
            valid = False
    return i

def MainMenu(c):
    print("Program Advisory Tool - Database Administration Console")
    print("What would you like to manage?")
    print("(1) Manage Programs")
    print("(2) Manage Courses")
    choice = getIntegerChoice(1,2)
    if(choice == 1):
        ManageProgramsMenu(c)
    else:
        ManageCoursesMenu(c)

def ManageProgramsMenu(c):
    print("Current Programs:")
    displayProgramList(c)
    print("Manage which program? (0 = Create New Program)")
    choice = getIntegerChoice(0, GetNumPrograms(c))
    if(choice == 0):
        CreateProgramMenu(c)
    else:
        ManageProgramMenu(c, choice)
    
def CreateProgramMenu(c):
    print("Creating New Program...")
    name = input("Program Name: ")
    AddProgram(c, name)

def ManageProgramMenu(c, programID):
    print(f"Managing Program {programID}")
    displayProgramById(c, programID)
    print("(1) Manage Courses In Program")
    print("(2) Delete Program")
    choice = getIntegerChoice(1,2)
    if(choice == 1):
        ManageCoursesInProgramMenu(c, programID)
    else:
        DeleteProgramMenu(c, programID)

def ManageCoursesInProgramMenu(c, programID):
    print("Courses In Program")
    displayCoursesInProgram(c, programID)
    print("(1) Add a Course                 (2) Remove a Course")
    print("(3) Add Course To Directed Group (4) Remove Course From Directed Group")
    print("(5) Add Directed Group           (6) Remove Directed Group")
    choice = getIntegerChoice(1,6)
    if(choice == 1):
        AddCourseToProgramMenu(c, programID)
    elif(choice == 2):
        RemoveCourseFromProgramMenu(c, programID)
    elif(choice == 3):
        AddCourseToDirectedGroupMenu(c, programID)
    elif(choice == 4):
        RemoveCourseFromDirectedGroupMenu(c, programID)
    elif(choice == 5):
        AddDirectedGroupToProgramMenu(c, programID)
    else:
        RemoveDirectedGroupFromProgramMenu(c, programID)

def AddCourseToProgramMenu(c, programID):
    print("Adding Course To Program...")
    inp = input("Course ID or Course Code: ")
    # Check for a number
    try:
        id = int(inp)
        # We have a number
        AddCourseToProgram(c, programID, id, 0)
    except ValueError:
        # We don't have a number - Course Code
        id = GetCourseIdByCourseCode(c, inp)
        AddCourseToProgram(c, programID, id, 0)


def RemoveCourseFromProgramMenu(c, programID):
    #TODO
    print("Remove Course From Program")

def AddCourseToDirectedGroupMenu(c, programID):
    #TODO
    print("Add Course To Directed Group")

def RemoveCourseFromDirectedGroupMenu(c, programID):
    #TODO
    print("Add Course To Program")

def AddDirectedGroupToProgramMenu(c, programID):
    #TODO
    print("Add Directed Group To Program")

def RemoveDirectedGroupFromProgramMenu(c, programID):
    #TODO
    print("Remove Directed Group From Program")

def DeleteProgramMenu(c, programID):
    #TODO
    print("Are you sure?")

def ManageCoursesMenu(c):
    #TODO
    print("Course Management")