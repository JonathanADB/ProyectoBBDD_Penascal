from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .routers import courses, admin
from .db import engine, Base
from .dependencies import get_db
from . import crud

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

#Admin
@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
#Create
@app.get("/admin/create_course", response_class=HTMLResponse)
async def create_course_form(request: Request):
    return templates.TemplateResponse("create_course.html", {"request": request})

@app.get("/admin/create_professor", response_class=HTMLResponse)
async def create_professor_form(request: Request):
    return templates.TemplateResponse("create_professor.html", {"request": request})

@app.get("/admin/create_student", response_class=HTMLResponse)
async def create_student_form(request: Request):
    return templates.TemplateResponse("create_student.html", {"request": request})

#Update
@app.get("/admin/update_course", response_class=HTMLResponse)
async def update_course_form(request: Request):
    return templates.TemplateResponse("update_entity.html", {"request": request})

@app.get("/admin/update_professor", response_class=HTMLResponse)
async def update_professor_form(request: Request):
    return templates.TemplateResponse("update_entity.html", {"request": request})

@app.get("/admin/update_student", response_class=HTMLResponse)
async def update_student_form(request: Request):
    return templates.TemplateResponse("update_entity.html", {"request": request})