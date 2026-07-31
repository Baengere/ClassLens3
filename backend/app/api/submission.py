from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.db import SessionLocal
from app.schemas.submission import SubmissionResponse, SubmissionUpdate, SubmissionDetailResponse
from app.services.submission_service import get_submissions, update_teacher_mark
from app.services.submission_service import create_submission
from app.services.submission_service import get_submission
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SubmissionResponse)
async def create_new_submission(
    question_id:int = Form(...),
    image:UploadFile = File(...),
    db: Session = Depends(get_db)
):
    #Create Uploads folder if needed
    import os
    import uuid

    os.makedirs("uploads", exist_ok=True)

    filename = f"{uuid.uuid4()}.jpg"
    filepath = os.path.join("uploads", filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await image.read())

    submission = create_submission(
        db=db,
        question_id =question_id,
        image_path=filepath
    )
    return submission

@router.get("/{question_id}",response_model=list[SubmissionResponse])
def read(question_id:int, db: Session = Depends(get_db)):
    return get_submissions(db, question_id)


@router.patch("/{submission_id}",response_model=SubmissionResponse)
def mark_submission(submission_id:int,data:SubmissionUpdate,db: Session = Depends(get_db)):
    submission = update_teacher_mark(
        db,
        submission_id,
        data.teacher_mark
    )

    return submission

@router.get("/detail/{submission_id}",response_model=SubmissionDetailResponse)

def read_submission(submission_id:int,db:Session = Depends(get_db)):
    return get_submission(db, submission_id)