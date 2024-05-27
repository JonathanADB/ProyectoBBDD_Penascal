# init_db.py
from sqlalchemy.orm import Session
from . import models, schemas, crud, db

def init_db():
    db_session = db.SessionLocal()
    try:
        # Crear 20 profesores
        for i in range(1, 21):
            if not crud.get_professor(db_session, i):
                professor = schemas.ProfessorCreate(name=f"Professor {i}", email=f"professor{i}@example.com")
                crud.create_professor(db_session, professor)
        
        # Crear 20 estudiantes
        for i in range(1, 21):
            if not crud.get_student(db_session, i):
                student = schemas.StudentCreate(name=f"Student {i}", email=f"student{i}@example.com")
                crud.create_student(db_session, student)
        
        # Crear 20 cursos
        for i in range(1, 21):
            if not crud.get_course(db_session, i):
                course = schemas.CourseCreate(title=f"Course {i}", description=f"Description for Course {i}", professor_id=(i % 20) + 1)
                crud.create_course(db_session, course)
    finally:
        db_session.close()
