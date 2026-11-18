
import os


def calculate_semantic_similarity(resume_text, job_description):

    # Disable the heavy model on the hosted server when configured
    if os.environ.get("DISABLE_SEMANTIC_MODEL") == "1":
        return None

    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity

    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device="cpu"
    )

    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_numpy=True
    )

    semantic_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    semantic_percentage = semantic_score * 100

    return round(semantic_percentage, 2)


if __name__ == "__main__":

    resume_text = "Developed predictive models using Python."
    job_description = "Experience in machine learning algorithms."

    score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    if score is None:
        print("Semantic Similarity: Disabled")
    else:
        print("Semantic Similarity Score:", score, "%")
