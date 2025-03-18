from app import connection
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.id'), nullable=False)
    city = Column(String(100), nullable=True)

    faculty = relationship("Faculty")

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"



class Student:
    def __init__(self, student_id, first_name, last_name, faculty_id):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.faculty_id = faculty_id

    @staticmethod
    def get_all():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()

    @staticmethod
    def get_by_id(student_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
            return cursor.fetchone()

    def save(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO students (first_name, last_name, faculty_id) VALUES (%s, %s, %s)",
                (self.first_name, self.last_name, self.faculty_id),
            )
            connection.commit()

    def update(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE students SET first_name = %s, last_name = %s, faculty_id = %s WHERE student_id = %s",
                (self.first_name, self.last_name, self.faculty_id, self.student_id),
            )
            connection.commit()

    @staticmethod
    def delete(student_id):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            connection.commit()