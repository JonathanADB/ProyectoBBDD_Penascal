from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class ProfessorBase(BaseModel):
    name: str
    email: str

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str
    professor_id: Optional[int] = None

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    professor: Optional[Professor]

    class Config:
        orm_mode = True

class Enrollment(BaseModel):
    student_id: int
    course_id: int

    class Config:
        orm_mode = True
