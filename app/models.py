from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Especifica la longitud máxima como 50 caracteres
    email = Column(String(100), unique=True, index=True)  # Por ejemplo, 100 caracteres

class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Por ejemplo, 50 caracteres
    email = Column(String(100), unique=True, index=True)  # Por ejemplo, 100 caracteres

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)  # Por ejemplo, 100 caracteres
    description = Column(String(255), index=True)  # Por ejemplo, 255 caracteres
    professor_id = Column(Integer, ForeignKey('professors.id'))
    professor = relationship("Professor")

class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student = relationship("Student")
    course = relationship("Course")
