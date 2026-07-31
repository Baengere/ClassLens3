from pydantic import BaseModel
from datetime import datetime

class QuestionCreate(BaseModel):
    assignment_id: int
    question_text: str
    model_answer: str
    rubric: str
    marks: int

class QuestionResponse(BaseModel):
    id: int
    assignment_id: int
    question_text: str
    model_answer: str
    rubric:str
    marks: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
