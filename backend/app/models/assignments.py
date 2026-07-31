from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db import Base

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255),nullable=False)
    subject = Column(String(100),nullable=False)
    description = Column(Text,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
 