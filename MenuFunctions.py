from displayFunctions import *
from databaseFunctions import *

def getIntegerChoiceNoMax(minRange):
    valid = False
    while(not valid):
        try:
            i = int(input(f'Choice ({minRange}+): '))
        except ValueError:
            print("Invalid Input: Please input a number")
            valid = False
            continue
        # We have a valid number, check range
        if(i >= minRange):
            valid = True
        else:
            print("Invalid Input: Too Low")
            valid = False
    return i

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

def getCourseIDWithOptionalCourseCode(c):
    inp = input("Course ID or Course Code: ")
    # Check for a number
    try:
        id = int(inp)
        # We have a number
    except ValueError:
        # We don't have a number - Course Code
        id = GetCourseIdByCourseCode(c, inp)
    return id

# Returns Whether or not we want to commit changes
def MainMenu(c):
    while True:
        print("Program Advisory Tool - Database Administration Console")
        print("What would you like to manage?")
        print("(1) Manage Programs")
        print("(2) Manage Courses")
        print("(3) Discard Changes and Quit")
        print("(4) Save And Quit")
        choice = getIntegerChoice(1,4)
        if(choice == 1):
            ManageProgramsMenu(c)
        elif(choice == 2):
            ManageCoursesMenu(c)
        elif(choice == 3):
            return False
        else:
            return True

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
    id = getCourseIDWithOptionalCourseCode(c)
    AddCourseToProgram(c, programID, id, 1)

def RemoveCourseFromProgramMenu(c, programID):
    print("Remove Which Course?")
    id = getCourseIDWithOptionalCourseCode(c)
    RemoveCourseFromProgram(c, programID, id)

def AddCourseToDirectedGroupMenu(c, programID):
    print("Which Course?")
    courseId = getCourseIDWithOptionalCourseCode(c)
    numGroups = GetNumDirectedGroupsByProgram(c, programID)
    groupNum = getIntegerChoice(1, numGroups)
    SetCourseInDirectedGroup(c, programID, courseId, groupNum)

def RemoveCourseFromDirectedGroupMenu(c, programID):
    # Note: This is just "Adding" a course to directed group 0
    print("Which Course?")
    courseId = getCourseIDWithOptionalCourseCode(c)
    SetCourseInDirectedGroup(c, programID, courseId, 0)

def AddDirectedGroupToProgramMenu(c, programID):
    print("Current Groups:")
    displayDirectedGroupsByProgram(c, programID)
    print("How many courses must be completed?")
    numCourses = getIntegerChoiceNoMax(1)
    # Due to database structure we need to auto-increment the group numbers (ew)
    nextGroup = CalculateNextDirectedGroupNumber(c, programID)
    AddDirectedGroupToProgram(c, programID, nextGroup, numCourses)

def RemoveDirectedGroupFromProgramMenu(c, programID):
    print("Current Groups:")
    displayDirectedGroupsByProgram(c, programID)
    print("Delete Which Group?")
    choice = getIntegerChoice(1, GetNumDirectedGroupsByProgram(c, programID))
    RemoveDirectedGroupFromProgram(c, programID, choice)
    # Remove The Courses
    RemoveAllCoursesFromProgramByDirectedGroup(c, programID, choice)

def DeleteProgramMenu(c, programID):
    # Delete All Directed Groups, Delete All Courses In Program, Delete Program
    RemoveAllDirectedGroupsFromProgram(c, programID)
    RemoveAllCoursesFromProgram(c, programID)
    RemoveProgram(c, programID)
    print("Program Deleted")

def ManageCoursesMenu(c):
    #TODO
    print("Course Management")