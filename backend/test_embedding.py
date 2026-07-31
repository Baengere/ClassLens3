from app.processing.embeddings import create_embedding
from app.processing.similarity import cosine_similarity

teacher = create_embedding(
    "Photosynthesis is the process by which plants use sunlight, water and carbon dioxide to produce glucose."
)

student = create_embedding(
    "The capital city of Kenya is Nairobi."
)

score = cosine_similarity(teacher, student)

print(f"Similarity: {score:.4f}")