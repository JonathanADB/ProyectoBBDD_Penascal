from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
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
