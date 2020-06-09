
def GetProgramIDByName(c, ProgramName):
    c.execute('SELECT id FROM Programs WHERE Program_Name = ?', (ProgramName,))
    return c.fetchone()[0]

# What would we like to do?
# 1. Program Management
#    - View Programs
def GetPrograms(c):
  res = c.execute('''SELECT * FROM PROGRAMS''')
  return res

#    - Add Program
def AddProgram(c, programName):
  c.execute('INSERT INTO Programs(Program_Name) VALUES (?)', (programName,))
  return

#    - Remove Program
def RemoveProgram(c, ProgramName):
    c.execute('DELETE FROM Programs WHERE Program_Name = ?', (ProgramName,))
    return

#    - View Courses in Program
def GetProgramsInCourse(c, programID):
    return c.execute('SELECT * FROM Course_In_Program JOIN Courses ON Course_In_Program.Course_ID = Courses.ID WHERE Course_In_Program.Program_ID = ?', (programID,))

#    - Add Course to Program
def AddCourseToProgram(c, programID, courseID, directedGroup):
    c.execute('INSERT INTO Course_In_Program(program_id, course_id, directed_group) VALUES (?,?,?)', (programID, courseID, directedGroup))
    return

#    - Remove Course from program
def RemoveCourseFromProgram(c, programID, courseID):
    c.execute('DELETE FROM Course_In_Program WHERE program_id = ? AND course_id = ?', (programID, courseID))
    return

#    - View Directed Groups for Program
def GetDirectedGroupsByProgram(c, programID):
    # return c.execute('SELECT Course_In_Program.directed_group as group_id, count(id) as count FROM Course_In_Program JOIN Courses ON Course_In_Program.Course_ID = Courses.ID WHERE Course_In_Program.Program_ID = ? GROUP BY directed_group;', (programID,))
    return c.execute('SELECT * FROM Directed_Course_Requirements WHERE program_id = ?', (programID,))

#    - View Courses In Directed Group
def GetCoursesInDirectedGroup(c, programID, directedGroup):
    return c.execute('SELECT * FROM Course_In_Program JOIN Courses ON Course_In_Program.Course_ID = Courses.ID WHERE Course_In_Program.Program_ID = ? AND Course_In_Program.directed_group = ?', (programID, directedGroup))

#    - Add Directed Group
def AddDirectedGroupToProgram(c, programID, groupNumber, requiredCourses):
    c.execute('INSERT INTO Directed_Course_Requirements(program_id, directed_group, number_required) VALUES (?, ?, ?)', (programID, groupNumber, requiredCourses))
    return

#    - Remove Directed Group
def RemoveDirectedGroupFromProgram(c, programID, groupNumber):
    c.execute('DELETE FROM Directed_Course_Requirements WHERE program_id = ? AND directed_group = ?', (programID, groupNumber))
    return