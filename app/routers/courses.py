from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, dependencies

router = APIRouter()

@router.get("/", response_model=List[schemas.Course])
async def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.post("/enroll/", response_model=schemas.Enrollment)
async def enroll_student(enrollment: schemas.Enrollment, db: Session = Depends(dependencies.get_db)):
    return crud.enroll_student(db, student_id=enrollment.student_id, course_id=enrollment.course_id)
