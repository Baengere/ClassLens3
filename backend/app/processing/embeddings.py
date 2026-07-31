from fastembed import TextEmbedding

# Load the embedding model once when the application starts
embedding_model = TextEmbedding()


def create_embedding(text: str):
    """
    Generate an embedding for a piece of text.
    """

    embedding = next(embedding_model.embed([text]))

    return embedding