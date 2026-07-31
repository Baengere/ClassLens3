from sqlalchemy.orm import Session
from app.models import Submission

def create_submission(
        db: Session,
        question_id: int,
        image_path: str,
        ocr_text: str | None = None,
):
    submission = Submission(
        question_id = question_id,
        image_path = image_path,
        ocr_text = ocr_text,
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return submission

def update_submission(
        db,
        submission,
        ocr_text=None,
        similarity_score=None,
        suggested_mark=None
):
    if ocr_text is not None:
        submission.ocr_text = ocr_text

    if similarity_score is not None:
        submission.similarity_score = similarity_score

    if suggested_mark is not None:
        submission.suggested_mark = suggested_mark

    db.commit()
    db.refresh(submission)

    return submission 


def get_submissions(db:Session, question_id:int):
    return(
        db.query(Submission)
        .filter(Submission.question_id == question_id)
        .order_by(Submission.created_at.desc())
        .all()
    )

def save_submission(db:Session, submission:Submission):
    db.commit()
    db.refresh(submission)
    return submission


def update_teacher_mark(db, submission_id, teacher_mark):
    submission = (
        db.query(Submission)
        .filter(Submission.id == submission_id)
        .first()
    )

    if submission is None:
        return None

    submission.teacher_mark = teacher_mark
    submission.status = "completed"

    db.commit()
    db.refresh(submission)

    return submission

def get_submission(db, submission_id):
    return(
        db.query(Submission)
        .filter(Submission.id == submission_id)
        .first()
    )