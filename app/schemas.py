from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True

class ProfessorBase(BaseModel):
    name: str
    email: str

class ProfessorCreate(ProfessorBase):
    pass

class Professor(ProfessorBase):
    id: int

    class Config:
        from_attributes = True

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
        from_attributes = True

class Enrollment(BaseModel):
    student_id: int
    course_id: int

    class Config:
        from_attributes = True

class CourseUpdate(CourseBase):
    title: Optional[str] = None
    description: Optional[str] = None
    professor_id: Optional[int] = None

    class Config:
        from_attributes = True