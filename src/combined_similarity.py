
from tfidf_similarity import calculate_text_similarity
from semantic_similarity import calculate_semantic_similarity


def calculate_combined_similarity(resume_text, job_description):
    tfidf_score = calculate_text_similarity(
        resume_text,
        job_description
    )

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    combined_score = (
        0.5 * tfidf_score +
        0.5 * semantic_score
    )

    return round(combined_score, 2)


resume_text = "Developed predictive models using Python."
job_description = "Experience in machine learning algorithms."

tfidf_score = calculate_text_similarity(
    resume_text,
    job_description
)

semantic_score = calculate_semantic_similarity(
    resume_text,
    job_description
)

combined_score = calculate_combined_similarity(
    resume_text,
    job_description
)

print("TF-IDF Similarity:", tfidf_score, "%")
print("Semantic Similarity:", semantic_score, "%")
print("Combined Similarity:", combined_score, "%")
