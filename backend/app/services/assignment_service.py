from sqlalchemy.orm import Session

from app.models import Assignment
from app.schemas import AssignmentCreate

def create_assignment(db: Session, assignment: AssignmentCreate):
    db_assignment = Assignment(
        title = assignment.title,
        subject = assignment.subject,
        description = assignment.description
    )

    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    
    return db_assignment

def get_assignments(db: Session):
    return db.query(Assignment).order_by(Assignment.created_at.desc()).all()

def get_assignment(db: Session, assignment_id: int):
    return (
        db.query(Assignment)
        .filter(Assignment.id == assignment_id)
        .first()
    )