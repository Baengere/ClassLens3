from datetime import datetime
from pydantic import BaseModel
from app.schemas.question import QuestionResponse

class SubmissionCreate(BaseModel):
    question_id: int

class SubmissionResponse(BaseModel):
    id: int
    question_id: int
    image_path: str
    ocr_text: str| None = None
    similarity_score: float | None = None
    suggested_mark: int | None = None
    teacher_mark:int | None = None
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class SubmissionUpdate(BaseModel):
    teacher_mark: int

class SubmissionDetailResponse(BaseModel):
    id:int

    question_id: int

    image_path:str

    ocr_text:str | None = None

    similarity_score:float | None = None

    suggested_mark:int | None = None

    teacher_mark:int | None = None

    status:str

    created_at: datetime

    question: QuestionResponse

    model_config = {
        "from_attributes":True
    }