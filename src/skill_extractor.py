
import re


# ==========================================
# 1. SKILLS DATABASE
# ==========================================

SKILLS_DATABASE = [

    # Programming Languages
    "Python",
    "SQL",
    "Java",
    "JavaScript",
    "C++",
    "C#",
    "C",
    "R",
    "TypeScript",

    # Frontend Development
    "HTML",
    "CSS",
    "React.js",
    "Bootstrap",
    "Tailwind CSS",
    "Responsive Web Design",
    "DOM Manipulation",
    "UI/UX Design",
    "Frontend Development",
    "User Interface",
    "User Experience",

    # Backend and Web Development
    "Flask",
    "Django",
    "REST API",
    "Node.js",
    "Express.js",
    "PHP",

    # Data Analysis
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Excel",
    "Advanced Excel",
    "Power BI",
    "Tableau",
    "Power Query",
    "DAX",
    "Data Analysis",
    "Data Cleaning",
    "Data Preprocessing",
    "Data Visualization",
    "Statistical Analysis",
    "Statistics",
    "Exploratory Data Analysis",

    # Machine Learning and AI
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Scikit-Learn",
    "TensorFlow",
    "PyTorch",
    "Random Forest",
    "Classification",
    "Regression",
    "Natural Language Processing",
    "Computer Vision",
    "Neural Networks",

    # Databases and Tools
    "MySQL",
    "SQLite",
    "MongoDB",
    "PostgreSQL",
    "Oracle Database",
    "Git",
    "GitHub",
    "Jupyter Notebook",
    "VS Code",
    "Chart.js",

    # Cloud Computing
    "AWS",
    "Microsoft Azure",
    "Google Cloud",

    # DevOps
    "Docker",
    "Kubernetes",
    "CI/CD",
    "Jenkins",
    "Linux",

    # Data Engineering
    "Apache Spark",
    "Hadoop",
    "ETL",
    "Data Warehousing",
    "Apache Kafka",

    # Project Management
    "Agile",
    "Scrum",
    "Jira",

    # Soft Skills
    "Communication",
    "Problem Solving",
    "Analytical Thinking",
    "Attention to Detail"
]


# ==========================================
# 2. SKILL ALIASES
# ==========================================

SKILL_ALIASES = {

    # HTML and CSS
    "html5": "HTML",
    "css3": "CSS",

    # JavaScript
    "js": "JavaScript",
    "reactjs": "React.js",
    "react js": "React.js",

    # Machine Learning
    "sklearn": "Scikit-Learn",
    "scikit learn": "Scikit-Learn",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "nlp": "Natural Language Processing",

    # Data Analysis
    "powerbi": "Power BI",
    "eda": "Exploratory Data Analysis",

    # Cloud
    "amazon web services": "AWS",
    "gcp": "Google Cloud",

    # Databases
    "postgres": "PostgreSQL",

    # Frontend
    "tailwind": "Tailwind CSS",
    "ui ux design": "UI/UX Design"
}


# ==========================================
# 3. CHECK WHETHER A SKILL EXISTS
# ==========================================

def contains_skill(text, skill):

    pattern = (
        r"(?<!\w)"
        + re.escape(skill)
        + r"(?!\w)"
    )

    return re.search(
        pattern,
        text,
        re.IGNORECASE
    ) is not None


# ==========================================
# 4. EXTRACT SKILLS FROM TEXT
# ==========================================

def extract_skills(text):

    if not isinstance(text, str) or not text.strip():
        return []

    extracted_skills = []

    # Search the main skills database
    for skill in SKILLS_DATABASE:

        if contains_skill(text, skill):

            extracted_skills.append(skill)

    # Search alternative skill names
    for alias, standard_skill in SKILL_ALIASES.items():

        if contains_skill(text, alias):

            extracted_skills.append(standard_skill)

    # Remove duplicate skills while preserving order
    extracted_skills = list(
        dict.fromkeys(extracted_skills)
    )

    return extracted_skills


# ==========================================
# 5. TEST THE SKILL EXTRACTOR
# ==========================================

if __name__ == "__main__":

    sample_text = """
    I have experience in Python, SQL, HTML5 and CSS3.

    I have worked with Pandas, NumPy, Matplotlib,
    Machine Learning and Scikit-Learn.

    I also have knowledge of NLP, AWS, Docker,
    Kubernetes, Power BI, Excel and PostgreSQL.

    My technical tools include GitHub, Linux,
    Apache Spark, Jira and Agile.

    I know C programming and R programming.
    I use AI tools and JavaScript.

    I have also worked with ReactJS, Bootstrap,
    Tailwind CSS, TypeScript and Responsive Web Design.
    """

    skills = extract_skills(sample_text)

    print("\n========== ORIGINAL TEXT ==========\n")
    print(sample_text)

    print("\n========== EXTRACTED SKILLS ==========\n")

    for skill in skills:
        print("-", skill)

    print("\n====================================")
    print("TOTAL SKILLS FOUND:", len(skills))
