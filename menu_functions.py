from display_functions import *
from database_functions import *

def get_integer_choice_no_max(min_range):
    valid = False
    while not valid:
        try:
            i = int(input(f'Choice ({min_range}+): '))
        except ValueError:
            print("Invalid Input: Please input a number")
            valid = False
            continue
        # We have a valid number, check range
        if i >= min_range:
            valid = True
        else:
            print("Invalid Input: Too Low")
            valid = False
    return i

def get_integer_choice(min_range, max_range):
    valid = False
    while not valid:
        try:
            i = int(input(f'Choice ({min_range} - {max_range}): '))
        except ValueError:
            print("Invalid Input: Please input a number")
            valid = False
            continue
        # We have a valid number, check range
        if(i >= min_range and i <= max_range):
            valid = True
        else:
            print("Invalid Input: Outside range")
            valid = False
    return i

def get_course_id_with_optional_course_code(c):
    inp = input("Course ID or Course Code: ")
    # Check for a number
    try:
        id = int(inp)
        # We have a number
    except ValueError:
        # We don't have a number - Course Code
        id = get_course_id_by_course_code(c, inp)
    return id

# Returns Whether or not we want to commit changes
def main_menu(c):
    while True:
        print("Program Advisory Tool - Database Administration Console")
        print("What would you like to manage?")
        print("(1) Manage Programs")
        print("(2) Manage Courses")
        print("(3) Discard Changes and Quit")
        print("(4) Save And Quit")
        choice = get_integer_choice(1, 4)
        if choice == 1:
            manage_programs_menu(c)
        elif choice == 2:
            manage_courses_menu(c)
        elif choice == 3:
            return False
        else:
            return True

def manage_programs_menu(c):
    print("Current Programs:")
    display_program_list(c)
    print("Manage which program? (0 = Create New Program)")
    choice = get_integer_choice(0, get_num_programs(c))
    if choice == 0:
        create_program_menu(c)
    else:
        manage_program_menu(c, choice)

def create_program_menu(c):
    print("Creating New Program...")
    name = input("Program Name: ")
    add_program(c, name)

def manage_program_menu(c, program_id):
    print(f"Managing Program {program_id}")
    display_program_by_id(c, program_id)
    print("(1) Manage Courses In Program")
    print("(2) Delete Program")
    choice = get_integer_choice(1, 2)
    if choice == 1:
        manage_courses_in_program_menu(c, program_id)
    else:
        delete_program_menu(c, program_id)

def manage_courses_in_program_menu(c, program_id):
    print("Courses In Program")
    display_courses_in_program(c, program_id)
    print("(1) Add a Course                 (2) Remove a Course")
    print("(3) Add Course To Directed Group (4) Remove Course From Directed Group")
    print("(5) Add Directed Group           (6) Remove Directed Group")
    choice = get_integer_choice(1, 6)
    if choice == 1:
        add_course_to_program_menu(c, program_id)
    elif choice == 2:
        remove_course_from_program_menu(c, program_id)
    elif choice == 3:
        add_course_to_directed_group_menu(c, program_id)
    elif choice == 4:
        remove_course_from_directed_group_menu(c, program_id)
    elif choice == 5:
        add_directed_group_to_program_menu(c, program_id)
    else:
        remove_directed_group_from_program_menu(c, program_id)

def add_course_to_program_menu(c, program_id):
    print("Adding Course To Program...")
    id = get_course_id_with_optional_course_code(c)
    add_course_to_program(c, program_id, id, 1)

def remove_course_from_program_menu(c, program_id):
    print("Remove Which Course?")
    id = get_course_id_with_optional_course_code(c)
    remove_course_from_program(c, program_id, id)

def add_course_to_directed_group_menu(c, program_id):
    print("Which Course?")
    course_id = get_course_id_with_optional_course_code(c)
    num_groups = get_num_directed_groups_by_program(c, program_id)
    group_num = get_integer_choice(1, num_groups)
    set_course_in_directed_group(c, program_id, course_id, group_num)

def remove_course_from_directed_group_menu(c, program_id):
    # Note: This is just "Adding" a course to directed group 0
    print("Which Course?")
    course_id = get_course_id_with_optional_course_code(c)
    set_course_in_directed_group(c, program_id, course_id, 0)

def add_directed_group_to_program_menu(c, program_id):
    print("Current Groups:")
    display_directed_groups_by_program(c, program_id)
    print("How many courses must be completed?")
    num_courses = get_integer_choice_no_max(1)
    # Due to database structure we need to auto-increment the group numbers (ew)
    next_group = calculate_next_directed_group_number(c, program_id)
    add_directed_group_to_program(c, program_id, next_group, num_courses)

def remove_directed_group_from_program_menu(c, program_id):
    print("Current Groups:")
    display_directed_groups_by_program(c, program_id)
    print("Delete Which Group?")
    choice = get_integer_choice(1, get_num_directed_groups_by_program(c, program_id))
    remove_directed_group_from_program(c, program_id, choice)
    # Remove The Courses
    remove_all_courses_from_program_by_directed_group(c, program_id, choice)

def delete_program_menu(c, program_id):
    # Delete All Directed Groups, Delete All Courses In Program, Delete Program
    remove_all_directed_groups_from_program(c, program_id)
    remove_all_courses_from_program(c, program_id)
    remove_program(c, program_id)
    print("Program Deleted")

def manage_courses_menu(c):
    print("Current Courses: ")
    display_course_list(c)
    print("Manage which course? (0 = Create New Course)")
    choice = get_integer_choice(0, get_num_courses(c))
    if choice == 0:
        create_course_menu(c)
    else:
        manage_course_menu(c, choice)

def create_course_menu(c):
    print("Creating New Course...")
    code = input("Course Code: ")
    name = input("Course Name: ")
    # Due to course code structure, year level is the fifth character in the code
    year_level = code[4]
    add_course(c, code, name, year_level)

def manage_course_menu(c, course_id):
    print(f'Managing Course #{course_id}')
    print("(1) Manage Precedents")
    print("(2) Delete Course")
    choice = get_integer_choice(1, 2)
    if choice == 1:
        manage_course_precedents_menu(c, course_id)
    else:
        delete_course_menu(c, course_id)

def manage_course_precedents_menu(c, course_id):
    print("Current Precedents")
    display_course_precedents(c, course_id)
    print("(1) Add Precedent          (2) Remove Precedent")
    print("(3) Add Precedent to Group (4) Remove Precedent From Group")
    choice = get_integer_choice(1, 4)
    if choice == 1:
        add_precedent_menu(c, course_id)
    elif choice == 2:
        remove_precedent_menu(c, course_id)
    elif choice == 3:
        set_precedent_group_menu(c, course_id)
    else:
        remove_precedent_group_menu(c, course_id)

def add_precedent_menu(c, course_id):
    print("Add which course as precedent?")
    id = get_course_id_with_optional_course_code(c)
    add_precedent_to_course(c, course_id, id, 0)

def remove_precedent_menu(c, course_id):
    print("Remove which course as precedent?")
    id = get_course_id_with_optional_course_code(c)
    remove_precedent_from_course(c, course_id, id)

def set_precedent_group_menu(c, course_id):
    print("Set group for which course?")
    id = get_course_id_with_optional_course_code(c)
    print("New Group #")
    group = get_integer_choice_no_max(1)
    set_course_precedence_group(c, course_id, id, group)

def remove_precedent_group_menu(c, course_id):
    print("Remove Which Course From its group?")
    id = get_course_id_with_optional_course_code(c)
    set_course_precedence_group(c, course_id, id, 0)

def delete_course_menu(c, course_id):
    # Delete course precedence records with this course
    # Both as a precedent, and as the successor
    remove_all_course_precedence_records_by_precedent(c, course_id)
    remove_all_course_precedence_records_by_successor(c, course_id)
    # Delete course from any program
    remove_course_from_all_programs(c, course_id)
    # Finally delete the course
    remove_course(c, course_id)
