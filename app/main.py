from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .routers import courses, admin
from .db import engine, Base
from .dependencies import get_db
from . import crud, schemas

app = FastAPI()

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")

app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    courses = crud.get_courses(db)
    return templates.TemplateResponse("index.html", {"request": request, "courses": courses})

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/admin/create_course", response_class=HTMLResponse)
async def create_course_form(request: Request):
    return templates.TemplateResponse("create_course.html", {"request": request})

@app.get("/admin/update_course/{course_id}", response_class=HTMLResponse)
async def update_course_form(request: Request, course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    professors = crud.get_professors(db)
    return templates.TemplateResponse("update_course.html", {"request": request, "course": course, "professors": professors})

@app.post("/admin/update_course/{course_id}", response_class=HTMLResponse)
async def update_course(request: Request, course_id: int, title: str = Form(...), description: str = Form(...), professor_id: int = Form(...), db: Session = Depends(get_db)):
    course_update = schemas.CourseUpdate(title=title, description=description, professor_id=professor_id)
    updated_course = crud.update_course(db, course_id, course_update)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return templates.TemplateResponse("update_course.html", {"request": request, "course": updated_course, "professors": crud.get_professors(db)})
