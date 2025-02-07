from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import random

DB_NAME = 'sqlite:///university.db'
Base = declarative_base()

# Проміжна таблиця для зв'язку "багато-до-багатьох"
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_courses, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=student_courses, back_populates='courses')

# Підключення до бази
engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def populate_db():
    courses = [Course(title=title) for title in ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']]
    session.add_all(courses)
    session.commit()

    students = [Student(name=f'Student {i}') for i in range(1, 21)]
    session.add_all(students)
    session.commit()

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))
    session.commit()

def add_student(name, course_ids):
    student = Student(name=name)
    student.courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    session.add(student)
    session.commit()
    print(f"Студент {name} успішно доданий!")

def get_students_by_course(course_id):
    course = session.get(Course, course_id)
    return [student.name for student in course.students] if course else []

def get_courses_by_student(student_id):
    student = session.get(Student, student_id)
    return [course.title for course in student.courses] if student else []

def update_student(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Ім'я студента оновлено на {new_name}")

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента {student_id} видалено")

if __name__ == "__main__":
    populate_db()
    add_student('Новий Студент', [1, 3])
    print("Студенти на курсі Mathematics:", get_students_by_course(1))
    print("Курси студента 2:", get_courses_by_student(2))
    update_student(2, "Оновлене Ім'я")
    delete_student(3)