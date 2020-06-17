# ======================================================================
# SELECT / GET
# ======================================================================
def get_program_id_by_name(c, program_name):
    c.execute('SELECT id FROM Programs WHERE name = ?', (program_name,))
    return c.fetchone()[0]

def get_programs(c):
    res = c.execute('SELECT * FROM PROGRAMS')
    return res

def get_program_by_id(c, program_id):
    c.execute('SELECT * FROM Programs WHERE id = ?', (program_id,))
    return c.fetchone()

def get_num_programs(c):
    c.execute('SELECT COUNT(id) FROM Programs')
    return c.fetchone()[0]

def get_courses_in_program(c, program_id):
    return c.execute('''SELECT
                        Courses.id AS id, 
                        Course_In_Program.directed_group AS dir, 
                        Courses.course_code AS course_code, 
                        Courses.name as name, 
                        Courses.year_level as year_level 
                    FROM 
                        Course_In_Program 
                    JOIN Courses ON Course_In_Program.Course_ID = Courses.ID 
                    WHERE Course_In_Program.Program_ID = ?''', (program_id,))

def get_directed_groups_by_program(c, program_id):
    return c.execute('SELECT directed_group AS grp_num, number_required AS requirement FROM Directed_Course_Requirements WHERE program_id = ?', (program_id,))

def get_num_directed_groups_by_program(c, program_id):
    c.execute('SELECT count(directed_group) FROM Directed_Course_Requirements WHERE program_id = ?', (program_id,))
    return c.fetchone()[0]

def get_courses_in_directed_group(c, program_id, directed_group):
    return c.execute('''SELECT * FROM Course_In_Program JOIN Courses ON Course_In_Program.Course_ID = Courses.ID
    WHERE Course_In_Program.Program_ID = ? AND Course_In_Program.directed_group = ?''', (program_id, directed_group))

def get_courses(c):
    res = c.execute('''SELECT * FROM Courses''')
    return res

def get_course_id_by_course_code(c, course_code):
    c.execute('SELECT id FROM Courses WHERE course_code = ?', (course_code,))
    return c.fetchone()[0]

def get_course_precedents(c, course_id):
    return c.execute(
        '''SELECT
                b.id AS id,
                b.course_code as course_code,
                p.requirement_group AS grp,
                b.name AS name
            FROM
                course_precedence AS p
            JOIN courses AS a ON p.course_after_id = a.id
            JOIN courses AS b ON p.course_before_id = b.id
            WHERE a.id = ?''', (course_id,))

def get_num_courses(c):
    c.execute('SELECT Count(id) FROM Courses')
    return c.fetchone()[0]

def calculate_next_directed_group_number(c, program_id):
    c.execute('SELECT max(directed_group) FROM Directed_Course_Requirements WHERE program_id = ?', (program_id,))
    return c.fetchone()[0] + 1

# ======================================================================
# INSERT / ADD
# ======================================================================

def add_program(c, program_name):
    c.execute('INSERT INTO Programs(name) VALUES (?)', (program_name,))
    return

def add_course_to_program(c, program_id, course_id, directed_group):
    c.execute('INSERT INTO Course_In_Program(program_id, course_id, directed_group) VALUES (?,?,?)', (program_id, course_id, directed_group))
    return

def add_directed_group_to_program(c, program_id, group_number, required_courses):
    c.execute('INSERT INTO Directed_Course_Requirements(program_id, directed_group, number_required) VALUES (?, ?, ?)', (program_id, group_number, required_courses))
    return

def add_course(c, course_code, course_name, year_level):
    c.execute('INSERT INTO Courses(course_code, name, year_level) VALUES (?,?,?)', (course_code, course_name, year_level))
    return

def add_precedent_to_course(c, course_after_id, course_before_id, precedence_group):
    c.execute("INSERT INTO Course_Precedence (course_before_id, course_after_id, requirement_group, hard) VALUES (?,?,?,1)", (course_before_id, course_after_id, precedence_group))

# ======================================================================
# DELETE / REMOVE
# ======================================================================

def remove_program(c, program_id):
    c.execute('DELETE FROM Programs WHERE id = ?', (program_id,))
    return

def remove_course_from_program(c, program_id, course_id):
    c.execute('DELETE FROM Course_In_Program WHERE program_id = ? AND course_id = ?', (program_id, course_id))
    return

def remove_directed_group_from_program(c, program_id, group_number):
    c.execute('DELETE FROM Directed_Course_Requirements WHERE program_id = ? AND directed_group = ?', (program_id, group_number))
    return

# That's a mouthful
def remove_all_courses_from_program_by_directed_group(c, program_id, group_number):
    c.execute('DELETE FROM Course_In_Program WHERE program_id = ? AND directed_group = ?', (program_id, group_number))

def remove_all_directed_groups_from_program(c, program_id):
    c.execute('DELETE FROM Directed_Course_Requirements WHERE program_id = ?', (program_id,))

def remove_all_courses_from_program(c, program_id):
    c.execute('DELETE FROM Course_In_Program WHERE program_id = ?', (program_id,))

def remove_course(c, course_id):
    c.execute('DELETE FROM Courses WHERE id = ?', (course_id,))
    return

def remove_precedent_from_course(c, course_after_id, course_before_id):
    c.execute("DELETE FROM Course_Precedence WHERE course_before_id = ? AND course_after_id = ?", (course_before_id, course_after_id))

def remove_all_course_precedence_records_by_precedent(c, course_id):
    c.execute("DELETE FROM Course_Precedence WHERE course_before_id = ?", (course_id,))

def remove_all_course_precedence_records_by_successor(c, course_id):
    c.execute("DELETE FROM Course_Precedence WHERE course_after_id = ?", (course_id,))

def remove_course_from_all_programs(c, course_id):
    c.execute("DELETE FROM Course_In_Program WHERE course_id = ?", (course_id,))

# ======================================================================
# UPDATE / SET
# ======================================================================

def set_course_in_directed_group(c, program_id, course_id, group_number):
    c.execute('UPDATE Course_In_Program SET directed_group = ? WHERE program_id = ? AND course_id = ?', (group_number, program_id, course_id))

def set_course_precedence_group(c, course_after_id, course_before_id, precedence_group):
    c.execute("UPDATE Course_Precedence SET requirement_group = ? WHERE course_before_id = ? AND course_after_id = ?", (precedence_group, course_before_id, course_after_id))
