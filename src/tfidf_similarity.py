
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(resume_text, job_text):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0],
        tfidf_matrix[1]
    )

    return round(similarity[0][0] * 100, 2)


if __name__ == "__main__":
    resume_text = "Developed predictive models using Python."
    job_description = "Experience in machine learning algorithms."

    score = calculate_text_similarity(resume_text, job_description)

    print("TF-IDF Similarity Score:", score, "%")
