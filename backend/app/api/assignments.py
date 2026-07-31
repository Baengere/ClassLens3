from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import AssignmentCreate, AssignmentResponse
from app.services.assignment_service import (
    create_assignment, get_assignments, get_assignment
)

router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)

@router.post("/", response_model=AssignmentResponse)
def create(assignment:AssignmentCreate, db: Session = Depends(get_db)):
    return create_assignment(db, assignment)

@router.get("/", response_model=list[AssignmentResponse])
def list_assignments(db: Session = Depends(get_db)):
    return get_assignments(db)

@router.get("/{assignment_id}", response_model=AssignmentResponse)
def read_assignment(
    assignment_id: int,
    db: Session = Depends(get_db)
):
    return get_assignment(db, assignment_id)