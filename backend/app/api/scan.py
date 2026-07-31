from fastapi import APIRouter, UploadFile, File
from app.processing.ocr import extract_text
import shutil
import os

router = APIRouter(
    prefix="/scan",
    tags=["Scan"]
)

@router.post("/")
async def scan(image: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    text = extract_text(file_path)

    return {
        "ocr_text": text
    }