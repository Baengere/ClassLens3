from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AssignmentCreate(BaseModel):
    title: str
    subject: str
    description: Optional[str]=None

class AssignmentUpdate(BaseModel):
    title: Optional[str]=None
    subject: Optional[str]=None
    description:Optional[str]=None

class AssignmentResponse(BaseModel):
    id: int
    title: str
    subject: str
    description: Optional[str]
    created_at: datetime

    model_config = {
        "from_attributes": True
    }