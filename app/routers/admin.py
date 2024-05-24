from fastapi import APIRouter, Depends, Form, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .. import crud, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/create_course", response_model=schemas.Course)
async def create_course(
    title: str = Form(...), 
    description: str = Form(...), 
    professor_id: int = Form(...), 
    db: Session = Depends(dependencies.get_db)
):
    course = schemas.CourseCreate(title=title, description=description, professor_id=professor_id)
    return crud.create_course(db, course=course)

@router.post("/create_professor", response_model=schemas.Professor)
async def create_professor(
    name: str = Form(...), 
    email: str = Form(...), 
    db: Session = Depends(dependencies.get_db)
):
    professor = schemas.ProfessorCreate(name=name, email=email)
    return crud.create_professor(db, professor=professor)

@router.post("/create_student", response_model=schemas.Student)
async def create_student(
    name: str = Form(...), 
    email: str = Form(...), 
    db: Session = Depends(dependencies.get_db)
):
    student = schemas.StudentCreate(name=name, email=email)
    return crud.create_student(db, student=student)

@router.get("/list_students", response_class=HTMLResponse)
async def list_students(request: Request, db: Session = Depends(dependencies.get_db)):
    students = crud.get_students(db)
    return templates.TemplateResponse("list_entities.html", {"request": request, "entities": students, "entity_type": "Students"})

@router.get("/list_professors", response_class=HTMLResponse)
async def list_professors(request: Request, db: Session = Depends(dependencies.get_db)):
    professors = crud.get_professors(db)
    return templates.TemplateResponse("list_entities.html", {"request": request, "entities": professors, "entity_type": "Professors"})

@router.get("/list_courses", response_class=HTMLResponse)
async def list_courses(request: Request, db: Session = Depends(dependencies.get_db)):
    courses = crud.get_courses(db)
    return templates.TemplateResponse("list_entities.html", {"request": request, "entities": courses, "entity_type": "Courses"})

@router.get("/update_student/{student_id}", response_class=HTMLResponse)
async def update_student_form(student_id: int, request: Request, db: Session = Depends(dependencies.get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return templates.TemplateResponse("update_entity.html", {"request": request, "entity": student, "entity_type": "Student"})

@router.post("/update_student/{student_id}", response_model=schemas.Student)
async def update_student(student_id: int, name: str = Form(...), email: str = Form(...), db: Session = Depends(dependencies.get_db)):
    student = schemas.StudentUpdate(name=name, email=email)
    return crud.update_student(db, student_id, student)

@router.post("/delete_student/{student_id}", response_model=schemas.Student)
async def delete_student(student_id: int, db: Session = Depends(dependencies.get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db, student_id)

@router.get("/update_professor/{professor_id}", response_class=HTMLResponse)
async def update_professor_form(professor_id: int, request: Request, db: Session = Depends(dependencies.get_db)):
    professor = crud.get_professor(db, professor_id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor not found")
    return templates.TemplateResponse("update_entity.html", {"request": request, "entity": professor, "entity_type": "Professor"})

@router.post("/update_professor/{professor_id}", response_model=schemas.Professor)
async def update_professor(professor_id: int, name: str = Form(...), email: str = Form(...), db: Session = Depends(dependencies.get_db)):
    professor = schemas.ProfessorUpdate(name=name, email=email)
    return crud.update_professor(db, professor_id, professor)

@router.post("/delete_professor/{professor_id}", response_model=schemas.Professor)
async def delete_professor(professor_id: int, db: Session = Depends(dependencies.get_db)):
    professor = crud.get_professor(db, professor_id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor not found")
    return crud.delete_professor(db, professor_id)

@router.get("/update_course/{course_id}", response_class=HTMLResponse)
async def update_course_form(course_id: int, request: Request, db: Session = Depends(dependencies.get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return templates.TemplateResponse("update_entity.html", {"request": request, "entity": course, "entity_type": "Course"})

@router.post("/update_course/{course_id}", response_model=schemas.Course)
async def update_course(course_id: int, title: str = Form(...), description: str = Form(...), professor_id: int = Form(...), db: Session = Depends(dependencies.get_db)):
    course = schemas.CourseUpdate(title=title, description=description, professor_id=professor_id)
    return crud.update_course(db, course_id, course)

@router.post("/delete_course/{course_id}", response_model=schemas.Course)
async def delete_course(course_id: int, db: Session = Depends(dependencies.get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.delete_course(db, course_id)
