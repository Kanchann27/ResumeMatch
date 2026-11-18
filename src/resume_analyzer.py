
from pathlib import Path

from tfidf_similarity import calculate_text_similarity
from semantic_similarity import calculate_semantic_similarity

from skill_matching import (
    compare_skills,
    calculate_skill_match_percentage
)

from pdf_extractor import extract_text_from_pdf
from skill_extractor import extract_skills
from skill_recommender import recommend_skills


def analyze_resume_job(resume_text, job_description):

    # 1. Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # 2. Calculate TF-IDF similarity
    tfidf_score = calculate_text_similarity(
        resume_text,
        job_description
    )

    # 3. Calculate semantic similarity
    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    # 4. Calculate combined similarity
    combined_score = round(
        (tfidf_score + semantic_score) / 2,
        2
    )

    # 5. Compare skills
    matching, missing, extra = compare_skills(
        resume_skills,
        job_skills
    )

    # 6. Calculate skill match percentage
    skill_percentage = calculate_skill_match_percentage(
        resume_skills,
        job_skills
    )

    # 7. Generate recommendations for missing skills
    recommendations = recommend_skills(missing)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "tfidf_similarity": tfidf_score,
        "semantic_similarity": semantic_score,
        "combined_text_similarity": combined_score,
        "matching_skills": matching,
        "missing_skills": missing,
        "extra_skills": extra,
        "skill_match_percentage": skill_percentage,
        "recommendations": recommendations
    }


if __name__ == "__main__":

    # Locate project folder
    project_folder = Path(__file__).resolve().parent.parent
    data_folder = project_folder / "data"

    # Find PDF resume
    pdf_files = list(data_folder.glob("*.pdf"))

    if len(pdf_files) == 0:

        print("No PDF resume found.")

    elif len(pdf_files) > 1:

        print("Multiple PDF files found. Keep only one PDF.")

    else:

        pdf_path = pdf_files[0]

        print("Reading resume:", pdf_path.name)

        # Extract resume text
        resume_text = extract_text_from_pdf(pdf_path)

        if not resume_text.strip():

            print("No text found in the PDF.")

        else:

            # Enter job description
            print("\n========== JOB DESCRIPTION ==========")
            print("Paste the job description below:")

            job_description = input("\n")

            if not job_description.strip():

                print("Job description cannot be empty.")

            else:

                # Analyze resume and job description
                results = analyze_resume_job(
                    resume_text,
                    job_description
                )

                # Display resume skills
                print("\n========== RESUME SKILLS ==========")
                print(results["resume_skills"])

                # Display job skills
                print("\n========== JOB SKILLS ==========")
                print(results["job_skills"])

                # Display similarity scores
                print("\n========== TEXT SIMILARITY RESULTS ==========")

                print(
                    "TF-IDF Similarity:",
                    results["tfidf_similarity"], "%"
                )

                print(
                    "Semantic Similarity:",
                    results["semantic_similarity"], "%"
                )

                print(
                    "Combined Text Similarity:",
                    results["combined_text_similarity"], "%"
                )

                # Display skill gap analysis
                print("\n========== SKILL GAP ANALYSIS ==========")

                print("Matching Skills:", results["matching_skills"])
                print("Missing Skills:", results["missing_skills"])
                print("Extra Skills:", results["extra_skills"])

                print(
                    "Skill Match Percentage:",
                    results["skill_match_percentage"], "%"
                )

                # Display skill recommendations
                print("\n========== SKILL GAP RECOMMENDATIONS ==========")

                if results["recommendations"]:

                    for skill, suggestions in results["recommendations"].items():

                        print(f"\nMissing Skill: {skill}")

                        for suggestion in suggestions:
                            print("-", suggestion)

                else:

                    print("No skill gaps found. Great job!")
