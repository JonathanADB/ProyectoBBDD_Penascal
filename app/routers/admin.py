from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/create_course/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_course(db, course=course)
