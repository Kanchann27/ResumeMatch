
# Skill recommendation module


# Recommendations for different skills
SKILL_RECOMMENDATIONS = {

    "data cleaning": [
        "Learn how to handle missing values using Pandas.",
        "Practice removing duplicate records.",
        "Learn how to detect and handle outliers.",
        "Practice correcting inconsistent data formats.",
        "Work with real-world datasets."
    ],

    "statistical analysis": [
        "Learn mean, median and mode.",
        "Understand variance and standard deviation.",
        "Learn correlation and covariance.",
        "Practice hypothesis testing.",
        "Understand t-tests and p-values."
    ],

    "machine learning": [
        "Learn supervised and unsupervised learning.",
        "Understand regression and classification.",
        "Practice Decision Tree and Random Forest algorithms.",
        "Learn model evaluation metrics.",
        "Build a small machine learning project."
    ],

    "python": [
        "Strengthen Python fundamentals.",
        "Practice functions, loops and data structures.",
        "Learn file handling and exception handling.",
        "Solve Python programming problems."
    ],

    "sql": [
        "Practice SELECT, WHERE and ORDER BY.",
        "Learn different types of JOIN operations.",
        "Practice GROUP BY and aggregate functions.",
        "Understand subqueries and SQL queries."
    ],

    "power bi": [
        "Learn data importing and transformation.",
        "Practice creating dashboards and visualizations.",
        "Learn Power Query.",
        "Understand basic DAX formulas."
    ],

    "excel": [
        "Practice Excel formulas and functions.",
        "Learn VLOOKUP and XLOOKUP.",
        "Practice Pivot Tables.",
        "Create charts and interactive reports."
    ],

    "pandas": [
        "Learn Series and DataFrame operations.",
        "Practice filtering and sorting data.",
        "Learn groupby and aggregation.",
        "Practice merging and joining datasets."
    ],

    "numpy": [
        "Learn NumPy arrays and array operations.",
        "Practice indexing and slicing.",
        "Understand broadcasting.",
        "Learn statistical functions in NumPy."
    ],

    "data visualization": [
        "Learn different types of charts.",
        "Practice creating visualizations using Matplotlib.",
        "Learn Seaborn for statistical plots.",
        "Practice presenting insights through dashboards."
    ]
}


def recommend_skills(missing_skills):

    recommendations = {}

    for skill in missing_skills:

        skill_key = skill.lower()

        if skill_key in SKILL_RECOMMENDATIONS:

            recommendations[skill] = SKILL_RECOMMENDATIONS[skill_key]

        else:

            recommendations[skill] = [
                f"Study the fundamentals of {skill}.",
                f"Practice {skill} through hands-on exercises.",
                f"Build a small project using {skill}."
            ]

    return recommendations


if __name__ == "__main__":

    # Sample missing skills
    missing_skills = [
        "Data Cleaning",
        "Statistical Analysis",
        "Power BI"
    ]

    # Generate recommendations
    results = recommend_skills(missing_skills)

    print("\n========== SKILL GAP RECOMMENDATIONS ==========")

    for skill, suggestions in results.items():

        print(f"\nMissing Skill: {skill}")

        for suggestion in suggestions:
            print("-", suggestion)
