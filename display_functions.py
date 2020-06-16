from database_functions import *

def print_labels_and_all_rows(rows, desc):
    for key in desc:
        print(key[0], end='\t')

    print('\n--------------------------------------------------------------------------------')

    for row in rows:
        for key in desc:
            print(row[key[0]], end='\t')
        print()

def print_labels_and_single_row(row, desc):
    for key in desc:
        print(key[0], end='\t')

    print('\n--------------------------------------------------------------------------------')

    for key in desc:
        print(row[key[0]], end='\t')
    print()

def display_program_list(c):
    rows = get_programs(c)
    print_labels_and_all_rows(rows, c.description)
    return

def display_program_by_id(c, program_id):
    row = get_program_by_id(c, program_id)
    print_labels_and_single_row(row, c.description)

def display_course_list(c):
    rows = get_courses(c)
    print_labels_and_all_rows(rows, c.description)
    return

def display_courses_in_program(c, program_id):
    rows = get_courses_in_program(c, program_id)
    print_labels_and_all_rows(rows, c.description)
    return

def display_course_precedents(c, course_id):
    rows = get_course_precedents(c, course_id)
    print_labels_and_all_rows(rows, c.description)
    return

def display_directed_groups_by_program(c, program_id):
    rows = get_directed_groups_by_program(c, program_id)
    print_labels_and_all_rows(rows, c.description)
    return
