from fastapi import APIRouter, Depends, UploadFile, File,Form
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.processing.grading import grade_submission

router = APIRouter(
    prefix="/grade",
    tags=["grading"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/")
def grade(
    question_id:int = Form(...),
    image:UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return grade_submission(
        db=db,
        question_id=question_id,
        image=image
    )