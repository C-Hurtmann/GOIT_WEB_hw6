from datetime import datetime
from random import randint, randrange
from sqlite3 import connect
from faker import Faker


STUDENTS_QTY = 50
TEACHERS_QTY = 5
SUBJECTS = ('Accounting',
            'Design',
            'Architecture',
            'Manufacturing Engineering',
            'Law',
            'Economics',
            'Medicine',
            'Computer Science')

fake = Faker()

def insert_data(sql, data):
    with connect('main.db') as con:
        cur = con.cursor()
        cur.executemany(sql, data)

def fill_groups():
    group_names = [('Alpha',) , ('Beta',), ('Gamma',)]
    with open('scripts/sql_frames/groups_filler.sql') as f:
        sql = f.read()
    insert_data(sql, group_names)
    print('Groups filled')

def fill_students(student_qty: int):
    students_data = []
    for _ in range(student_qty):
        student_data = (fake.name(),
                        fake.date_of_birth(minimum_age=18, maximum_age=40),
                        fake.email(),
                        fake.phone_number(),
                        randint(1, 3))
        students_data.append(student_data)
    with open('scripts/sql_frames/students_filler.sql') as f:
        sql = f.read()
    insert_data(sql, students_data)
    print('Students filled')

def fill_subjects(subjects: tuple, teacher_qty: int):
    with open('scripts/sql_frames/subjects_filler.sql') as f:
        sql = f.read()
    subjects_data = []
    teachers_id_list = list(range(1, teacher_qty+1))
    for i in subjects:
        try:
            teacher_id = teachers_id_list.pop(randint(0, len(teachers_id_list)))
        except IndexError:
            teacher_id = randint(1, teacher_qty)
        subjects_data.append((i, teacher_id))
    insert_data(sql, subjects_data)
    print('Subjects filled')

def fill_teachers(teacher_qty: int):
    teachers_data = []
    for _ in range(teacher_qty):
        teacher_data = ((fake.name(),))
        teachers_data.append(teacher_data)
    with open('scripts/sql_frames/teachers_filler.sql') as f:
        sql = f.read()
    insert_data(sql, teachers_data)
    print('Teachers filled')

def fill_grades(students_qty: int, subject_qty: int):
    grades_data = []
    for _ in range(20):
        for subject_id in range(1, subject_qty + 1):
            date = fake.date_between_dates(date_start=datetime(2023,4,1), date_end=datetime(2023,4,30))
            for student_id in range(1, students_qty + 1):
                come_to_class = fake.boolean()
                grade = randrange(5, 101, 5)
                if come_to_class:
                    grades_data.append((grade, date, subject_id, student_id))
    with open('scripts/sql_frames/grades_filler.sql') as f:
        sql = f.read()
    insert_data(sql, grades_data)
    print('Grades filled')


if __name__ == '__main__':
    fill_groups()
    fill_students(STUDENTS_QTY)
    fill_subjects(SUBJECTS, TEACHERS_QTY)
    fill_teachers(TEACHERS_QTY)
    fill_grades(STUDENTS_QTY, len(SUBJECTS))