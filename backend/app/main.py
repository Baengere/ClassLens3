from fastapi import FastAPI
from sqlalchemy import text
from app.db import Base, engine
from app.models import Assignment, Question
from app.api.assignments import router as assignments_router
from app.api.question import router as questions_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.scan import router as scan_router
from app.api.submission import router as submission_router
from app.api.grading import router as grading_router
from fastapi.staticfiles import StaticFiles
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
os.makedirs("uploads",exist_ok=True)
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
                              
)
                              

app.include_router(assignments_router)
app.include_router(questions_router)
app.include_router(scan_router)
app.include_router(submission_router)
app.include_router(grading_router)


@app.get("/")
def home():
    return {
          "message": "Welcome to ClassLens 3 🚀"
    }
@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return {
                "status": "Database Connected ✅"
            }
    except Exception as e:
        return {
            "status": "Database Connection Failed ❌",
            "error": str(e)
        }