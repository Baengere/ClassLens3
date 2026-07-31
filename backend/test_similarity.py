from app.processing.embeddings import create_embedding
from app.processing.similarity import cosine_similarity

model_answer = """
Photosynthesis is the process by which green plants use sunlight,
water and carbon dioxide to produce glucose and oxygen.
"""

student_answer = """
Plants make their own food using sunlight,
water and carbon dioxide.
"""

model_embedding = create_embedding(model_answer)
student_embedding = create_embedding(student_answer)

score = cosine_similarity(model_embedding, student_embedding)

print(f"Similarity score: {score:.4f}")