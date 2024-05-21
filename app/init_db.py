# init_db.py
from sqlalchemy.orm import Session
from . import models, schemas, crud, db

def init_db():
    db_session = db.SessionLocal()
    try:
        # Crear algunos datos de ejemplo
        if not crud.get_professor(db_session, 1):
            professor = schemas.ProfessorCreate(name="John Doe", email="john@example.com")
            crud.create_professor(db_session, professor)
        
        if not crud.get_student(db_session, 1):
            student = schemas.StudentCreate(name="Alice", email="alice@example.com")
            crud.create_student(db_session, student)
        
        if not crud.get_course(db_session, 1):
            course = schemas.CourseCreate(title="Math 101", description="Intro to Math", professor_id=1)
            crud.create_course(db_session, course)
    finally:
        db_session.close()
