from sqlalchemy import Column, Integer, Text, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db import Base
from sqlalchemy.orm import relationship


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False
    )

    question = relationship(
        "Question",
        back_populates="submissions"
    )

    image_path = Column(String, nullable=False)

    ocr_text = Column(Text)

    similarity_score = Column(Float)

    suggested_mark = Column(Integer)

    teacher_mark = Column(Integer)

    status = Column(String, default="pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )