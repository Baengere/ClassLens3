from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.schemas import QuestionCreate, QuestionResponse
from app.services.question_service import create_question, get_questions
from app.models import Question
from app.services.question_service import (create_question, get_questions, get_question)


router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_question(db:Session, question_id:int):
    return (
        db.query(Question)
        .filter(Question.id == question_id)
        .first()
    )

@router.post("/",response_model=QuestionResponse)
def create(
    question:QuestionCreate,
    db:Session = Depends(get_db)
):
    return create_question(db, question)


@router.get("/detail/{question_id}", response_model=QuestionResponse)
def read_question(question_id:int, db:Session=Depends(get_db)):
    return get_question(db,question_id)

@router.get("/{assignment_id}", response_model=list[QuestionResponse])
def read(assignment_id:int, db:Session = Depends(get_db)):
    return get_questions(db, assignment_id)