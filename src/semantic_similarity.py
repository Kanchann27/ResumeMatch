
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_semantic_similarity(resume_text, job_description):
    resume_embedding = model.encode(resume_text)
    job_embedding = model.encode(job_description)

    semantic_score = cosine_similarity(
        [resume_embedding],
        [job_embedding]
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

    print("Semantic Similarity Score:", score, "%")
