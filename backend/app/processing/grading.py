
from app.processing.storage import save_image
from app.processing.ocr import extract_text
from app.processing.embeddings import create_embedding
from app.processing.similarity import cosine_similarity

from app.services.submission_service import (
    create_submission,
    save_submission,
)

from app.services.question_service import get_question
def suggest_mark(similarity, total_marks):
    """Very simple MVP scorin
    To be replaced later with rubric-aware grading"""

    return round(similarity * total_marks)

def grade_submission(db, question_id, image):

    image_path = save_image(image)

    submission = create_submission(
        db=db,
        question_id=question_id,
        image_path=image_path,
    )

    ocr_text = extract_text(image_path)

    submission.ocr_text = ocr_text
    save_submission(db, submission)

    question = get_question(db, question_id)

    teacher_vector = create_embedding(
        question.model_answer
    )

    student_vector = create_embedding(
        submission.ocr_text
    )

    similarity = cosine_similarity(
        teacher_vector,
        student_vector,
    )

    submission.similarity_score = similarity

    submission.suggested_mark = suggest_mark(
        similarity,
        question.marks,
    )

    submission.status = "Completed"

    save_submission(db, submission)

    return submission