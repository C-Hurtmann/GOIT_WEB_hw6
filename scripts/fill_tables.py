from random import randint, randrange
from sqlite3 import connect
from faker import Faker


STUDENTS_QTY = 50
TEACHERS_QTY = 10
SUBJECTS = (('Accounting',),
            ('Design',),
            ('Architecture',),
            ('Manufacturing Engineering',),
            ('Law',),
            ('Economics',),
            ('Medicine',),
            ('Computer Science',))

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

def fill_students(qty):
    students_data = []
    for _ in range(qty):
        student_data = (fake.name(),
                        fake.date_of_birth(),
                        fake.email(),
                        fake.phone_number(),
                        randint(1, 3))
        students_data.append(student_data)
    with open('scripts/sql_frames/students_filler.sql') as f:
        sql = f.read()
    insert_data(sql, students_data)
    print('Students filled')

def fill_subjects():
    with open('scripts/sql_frames/subjects_filler.sql') as f:
        sql = f.read()
    insert_data(sql, SUBJECTS)
    print('Subjects filled')

def fill_teachers(qty):
    teachers_data = []
    subjects = list(range(1, 8+1))
    for _ in range(qty):
        try:
            random_subject = subjects.pop(randint(0, len(subjects)))
        except IndexError:
            random_subject = randint(1, 8)
        teacher_data = (fake.name(),
                        random_subject)
        teachers_data.append(teacher_data)
    with open('scripts/sql_frames/teachers_filler.sql') as f:
        sql = f.read()
    insert_data(sql, teachers_data)
    print('Teachers filled')

def fill_grades(students_qty, subject_qty):
    grades_data = []
    for student_id in range(1, students_qty + 1):
        for subject_id in range(1, subject_qty + 1):
            for _ in range(randint(1, 20)):
                grade = randrange(5, 101, 5)
                grades_data.append((grade, subject_id, student_id))
    with open('scripts/sql_frames/grades_filler.sql') as f:
        sql = f.read()
    insert_data(sql, grades_data)
    print('Grades filled')
if __name__ == '__main__':
    fill_grades(STUDENTS_QTY, len(SUBJECTS))