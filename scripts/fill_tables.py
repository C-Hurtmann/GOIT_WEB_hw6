from random import randint
from sqlite3 import connect
from faker import Faker


STUDENTS_QTY = 50
SUBJECTS_QTY = 8
TEACHERS_QTY = 5

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
    fake = Faker()
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

if __name__ == '__main__':
    fill_students(STUDENTS_QTY)