from app.models import Question
from app.schemas import QuestionCreate
from sqlalchemy.orm import Session
from app.processing.embeddings import create_embedding
import json



def create_question(db:Session, question: QuestionCreate):
    embedding = create_embedding(question.model_answer)
    embedding_json = json.dumps(embedding.tolist())

    db_question = Question (
        assignment_id = question.assignment_id,
        question_text = question.question_text,
        model_answer = question.model_answer,
        model_embedding =embedding_json,
        rubric = question.rubric,
        marks = question.marks

    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question

def get_questions(db: Session, assignment_id:int):
    return db.query(Question).filter(Question.assignment_id == assignment_id).order_by(Question.created_at.desc()).all()

def get_question(db: Session, question_id:int):
    return (
        db.query(Question)
        .filter(Question.id == question_id)
        .first()
    )

