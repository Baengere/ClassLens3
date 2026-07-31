from sqlalchemy import Column, Integer, String, ForeignKey,Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db import Base


class Question(Base):
    __tablename__ = "questions"
    submissions = relationship(
        "Submission",
        back_populates="question"
    )
    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"),nullable=False)
    question_text = Column(Text,nullable=False)
    model_answer = Column(Text, nullable=False)
    model_embedding = Column(Text)
    rubric = Column(Text, nullable=False)
    marks = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

