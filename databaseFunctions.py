
def GetProgramIDByName(c, ProgramName):
    c.execute('SELECT id FROM Programs WHERE Program_Name = ?', (ProgramName,))
    return c.fetchone()[0]

# 1. Program Management
def GetPrograms(c):
  res = c.execute('SELECT * FROM PROGRAMS')
  return res

def GetProgramById(c, programId):
    c.execute('SELECT * FROM Programs WHERE id = ?', (programId,))
    return c.fetchone()

def GetNumPrograms(c):
    c.execute('SELECT COUNT(id) FROM Programs')
    return c.fetchone()[0]

def AddProgram(c, programName):
  c.execute('INSERT INTO Programs(Program_Name) VALUES (?)', (programName,))
  return

def RemoveProgram(c, ProgramName):
    c.execute('DELETE FROM Programs WHERE Program_Name = ?', (ProgramName,))
    return

def GetCoursesInProgram(c, programID):
    return c.execute('''SELECT 
                        Courses.id AS id, 
                        Course_In_Program.directed_group AS dir, 
                        Courses.course_code AS course_code, 
                        Courses.name as name, 
                        Courses.year_level as year_level 
                    FROM 
                        Course_In_Program 
                    JOIN Courses ON Course_In_Program.Course_ID = Courses.ID 
                    WHERE Course_In_Program.Program_ID = ?''', (programID,))

def AddCourseToProgram(c, programID, courseID, directedGroup):
    c.execute('INSERT INTO Course_In_Program(program_id, course_id, directed_group) VALUES (?,?,?)', (programID, courseID, directedGroup))
    return

def RemoveCourseFromProgram(c, programID, courseID):
    c.execute('DELETE FROM Course_In_Program WHERE program_id = ? AND course_id = ?', (programID, courseID))
    return

def GetDirectedGroupsByProgram(c, programID):
    return c.execute('SELECT * FROM Directed_Course_Requirements WHERE program_id = ?', (programID,))

def GetCoursesInDirectedGroup(c, programID, directedGroup):
    return c.execute('SELECT * FROM Course_In_Program JOIN Courses ON Course_In_Program.Course_ID = Courses.ID WHERE Course_In_Program.Program_ID = ? AND Course_In_Program.directed_group = ?', (programID, directedGroup))

def AddDirectedGroupToProgram(c, programID, groupNumber, requiredCourses):
    c.execute('INSERT INTO Directed_Course_Requirements(program_id, directed_group, number_required) VALUES (?, ?, ?)', (programID, groupNumber, requiredCourses))
    return

def RemoveDirectedGroupFromProgram(c, programID, groupNumber):
    c.execute('DELETE FROM Directed_Course_Requirements WHERE program_id = ? AND directed_group = ?', (programID, groupNumber))
    return

# 2. Course Management:
def GetCourses(c):
  res = c.execute('''SELECT * FROM Courses''')
  return res

def AddCourse(c, courseCode, courseName, yearLevel):
  c.execute('INSERT INTO Courses(course_code, name, year_level) VALUES (?,?,?)', (courseCode, courseName, yearLevel))
  return

def RemoveCourse(c, courseId):
    c.execute('DELETE FROM Courses WHERE id = ?', (courseId,))
    return

def GetCoursePrecedents(c, courseID):
    return c.execute(
        '''SELECT 
                b.id AS id, 
                b.course_code as course_code, 
                b.name AS name 
            FROM 
                course_precedence AS p 
            JOIN courses AS a ON p.course_after_id = a.id 
            JOIN courses AS b ON p.course_before_id = b.id 
            WHERE a.id = ?''', (courseID,))
