# app/main.py
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

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/admin/create_course", response_class=HTMLResponse)
async def create_course_form(request: Request):
    return templates.TemplateResponse("create_course.html", {"request": request})