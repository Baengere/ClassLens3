import json
from app.processing.embeddings import create_embedding
from app.processing.similarity import cosine_similarity

def parse_rubric(rubric_text):
    """MVP. Treat the rubric column as json"""
    return json.loads(rubric_text)

def grade_criterion(student_embedding, criterion):
    criterion_embedding = create_embedding(
        criterion["criterion"]
    )

    similarity = cosine_similarity(
        student_embedding,
        criterion_embedding
    )

    return similarity

def award_marks(similarity, marks):
    if similarity > 0.80:
        return marks
    if similarity > 0.60:
        return round(marks * 0.5)

    return 0

def grade_rubric(student_text, rubric):

    student_embedding = create_embedding(student_text)
    results =[]

    total = 0

    for criterion in rubric:

        similarity = grade_criterion(
            student_embedding,
            criterion
        )

        awarded = award_marks(
            similarity,
            criterion["marks"]
        )

        total +=awarded

        results.append({
            "criterion":criterion["criterion"],
            "similarity":similarity,
            "awarded":awarded,
            "possible":criterion["marks"],
        }
        )

        return total, results