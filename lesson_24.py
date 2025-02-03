import sqlite3
import random

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS StudentCourses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    PRIMARY KEY (student_id, course_id)
)
''')

# Додавання курсів
courses = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
for course in courses:
    cursor.execute('INSERT INTO Courses (title) VALUES (?)', (course,))

# Додавання студентів
students = [f'Student {i}' for i in range(1, 21)]
for student in students:
    cursor.execute('INSERT INTO Students (name) VALUES (?)', (student,))

# Розподіл студентів по курсах
for student_id in range(1, 21):
    num_courses = random.randint(1, 3)  # Кожен студент може бути зареєстрований на 1-3 курси
    courses_ids = random.sample(range(1, 6), num_courses)
    for course_id in courses_ids:
        cursor.execute('INSERT INTO StudentCourses (student_id, course_id) VALUES (?, ?)', (student_id, course_id))

conn.commit()

# Функція для додавання нового студента та запису його на курс
def add_student(name, course_ids):
    cursor.execute('INSERT INTO Students (name) VALUES (?)', (name,))
    student_id = cursor.lastrowid
    for course_id in course_ids:
        cursor.execute('INSERT INTO StudentCourses (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
    conn.commit()
    print(f"Студент {name} успішно доданий і записаний на курси: {course_ids}")

# Функція для отримання студентів за курсом
def get_students_by_course(course_id):
    cursor.execute('''
    SELECT Students.name 
    FROM Students 
    JOIN StudentCourses ON Students.student_id = StudentCourses.student_id 
    WHERE StudentCourses.course_id = ?
    ''', (course_id,))
    return cursor.fetchall()

# Функція для отримання курсів за студентом
def get_courses_by_student(student_id):
    cursor.execute('''
    SELECT Courses.title 
    FROM Courses 
    JOIN StudentCourses ON Courses.course_id = StudentCourses.course_id 
    WHERE StudentCourses.student_id = ?
    ''', (student_id,))
    return cursor.fetchall()

# Функція для оновлення імені студента
def update_student(student_id, new_name):
    cursor.execute('UPDATE Students SET name = ? WHERE student_id = ?', (new_name, student_id))
    conn.commit()
    print(f"Ім'я студента з ID {student_id} оновлено на {new_name}")

# Функція для видалення студента
def delete_student(student_id):
    cursor.execute('DELETE FROM Students WHERE student_id = ?', (student_id,))
    cursor.execute('DELETE FROM StudentCourses WHERE student_id = ?', (student_id,))
    conn.commit()
    print(f"Студент з ID {student_id} успішно видалений")

# Приклади використання функцій
if __name__ == "__main__":
    add_student('Новий Студент', [1, 3])
    print("Студенти на курсі Mathematics (ID 1):", get_students_by_course(1))
    print("Курси студента з ID 2:", get_courses_by_student(2))
    update_student(2, 'Оновлене Ім\'я')
    delete_student(3)

conn.close()