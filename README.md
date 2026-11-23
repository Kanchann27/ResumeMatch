# ResumeMatch
### Resume–Job Description Matching and Skill Gap Analysis System

ResumeMatch is a web-based application developed to analyse resumes against job descriptions. It helps users evaluate how well their skills align with specific job requirements by identifying matching skills, missing skills, and textual similarity.

The application uses Python-based text processing and machine learning techniques to analyse resume content and generate structured results.

## Live Application

**Live Demo:** https://resumematch-xuxg.onrender.com

## Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Text Extraction:** Extract resume content using PyMuPDF.
- **Skill Extraction:** Identify technical and professional skills using predefined vocabulary and pattern-matching rules.
- **Skill Matching:** Compare resume skills with job requirements.
- **Text Similarity:** Use TF-IDF vectorization and cosine similarity to measure textual similarity.
- **Skill Gap Analysis:** Identify matched, missing, and additional skills.
- **Analysis History:** Store and retrieve previous analysis results using SQLite.
- **PDF Report Generation:** Generate downloadable reports containing analysis results.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| PDF Text Extraction | PyMuPDF |
| Text Processing | Regular Expressions |
| Machine Learning | Scikit-learn |
| Text Vectorization | TF-IDF |
| Similarity Measurement | Cosine Similarity |
| Semantic Model | Sentence Transformers |
| Database | SQLite |
| PDF Generation | ReportLab |
| Deployment | Render |
| Version Control | Git and GitHub |

## How It Works

1. **Resume Upload:** The user uploads a resume in PDF format.
2. **Text Extraction:** Resume content is extracted from the uploaded document.
3. **Skill Extraction:** Relevant skills are identified from the resume and job description.
4. **Skill Comparison:** Extracted skills are compared to identify matching and missing skills.
5. **Similarity Calculation:** TF-IDF vectorization and cosine similarity are used to measure textual similarity.
6. **Result Generation:** The application displays skill match percentage, text similarity, keyword overlap, and skill gap information.
7. **Report Generation:** Analysis results can be downloaded as a PDF report.
8. **History Management:** Previous analysis records can be viewed through the history page.

## Project Structure

```text
ResumeMatch/
│
├── app.py
│
├── src/
│   ├── pdf_extractor.py
│   ├── skill_extractor.py
│   ├── tfidf_similarity.py
│   ├── semantic_similarity.py
│   ├── skill_matching.py
│   ├── skill_recommender.py
│   ├── combined_similarity.py
│   ├── resume_analyzer.py
│   ├── database.py
│   └── pdf_report.py
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── data/
│
├── 01_data_exploration.ipynb
├── requirements.txt
└── README.md
```

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Kanchann27/ResumeMatch.git
cd ResumeMatch
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open the following address in your browser:

`http://127.0.0.1:5000`

## Deployment

The application is deployed on **Render** and connected to the GitHub repository.

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

The hosted application uses a lightweight configuration due to the memory limitations of the free hosting environment. TF-IDF-based similarity is used for the displayed text similarity score. The Sentence Transformers implementation is retained in the codebase but disabled in the hosted environment.

## Future Scope

- Support for additional resume formats, including DOCX.
- Improve skill extraction using advanced NLP techniques.
- Integrate semantic similarity into the hosted application.
- Enhance skill recommendations based on missing job requirements.
- Explore integration with external job portals.

## Project Information

- **Project Name:** ResumeMatch
- **Team Name:** JobFit
- **Institution:** Maharishi University of Information Technology
- **Academic Session:** 2023–2027

---

*ResumeMatch – Making resume analysis and job matching more effective.*
