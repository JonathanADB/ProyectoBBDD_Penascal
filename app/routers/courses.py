from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, dependencies

router = APIRouter()

@router.get("/", response_model=List[schemas.Course])
async def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.get("/students/", response_model=List[schemas.Student])
async def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@router.get("/professors/", response_model=List[schemas.Professor])
async def read_professors(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    professors = crud.get_professors(db, skip=skip, limit=limit)
    return professors
