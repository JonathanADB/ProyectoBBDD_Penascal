from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from typing import Optional 
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/create_course", response_model=schemas.Course)
async def create_course(
    title: str = Form(...), 
    description: str = Form(...), 
    professor_id: int = Form(...), 
    db: Session = Depends(dependencies.get_db)
):
    course = schemas.CourseCreate(title=title, description=description, professor_id=professor_id)
    return crud.create_course(db, course=course)

@router.put("/update_course/{course_id}", response_model=schemas.Course)
async def update_course(
    course_id: int,
    title: Optional[str] = Form(None), 
    description: Optional[str] = Form(None), 
    professor_id: Optional[int] = Form(None), 
    db: Session = Depends(dependencies.get_db)
):
    course_update = schemas.CourseUpdate(title=title, description=description, professor_id=professor_id)
    updated_course = crud.update_course(db, course_id, course_update)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course
