
def compare_skills(resume_skills, job_skills):
    matching = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    extra = list(set(resume_skills) - set(job_skills))

    return matching, missing, extra


def calculate_skill_match_percentage(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0.0

    matching, missing, extra = compare_skills(
        resume_skills,
        job_skills
    )

    percentage = (len(matching) / len(job_skills)) * 100

    return round(percentage, 2)


if __name__ == "__main__":
    resume_skills = ["Python", "SQL", "Excel", "Pandas"]
    job_skills = ["Python", "SQL", "Machine Learning", "Power BI"]

    matching, missing, extra = compare_skills(
        resume_skills,
        job_skills
    )

    skill_percentage = calculate_skill_match_percentage(
        resume_skills,
        job_skills
    )

    print("Matching Skills:", matching)
    print("Missing Skills:", missing)
    print("Extra Skills:", extra)
    print("Skill Match Percentage:", skill_percentage, "%")
