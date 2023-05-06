-- Table students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(30) NOT NULL,
    birthday DATE NOT NULL,
    phone VARCHAR(12) NOT NULL,
    email VARCHAR(20),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
);

-- Table groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title CHAR (2) NOT NULL
);

-- Table teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(30) NOT NULL,
    subject_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
);

-- Table subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (15) NOT NULl
);

-- Table grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade VARCHAR (2),
    subject_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE 
);