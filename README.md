# 🚀 ResumeMatch
### Resume–Job Description Matching and Skill Gap Analysis System

**Analyse Resumes | Match Job Requirements | Identify Skill Gaps**

ResumeMatch is a web-based application designed to analyse resumes against job descriptions and evaluate how well a candidate's skills align with specific job requirements.

The system combines Natural Language Processing (NLP), text processing and machine learning techniques to identify matching skills, missing skills and textual similarity between resumes and job descriptions.

It helps candidates understand their suitability for a particular job and identify areas where their skills can be improved.

---

## 🌐 Live Application

ResumeMatch is successfully deployed on **Render** and is accessible through the following link:

<https://resumematch-xuxg.onrender.com>

### 🚀 [Click Here to Open ResumeMatch – Live Demo](https://resumematch-xuxg.onrender.com)

**What you can explore:**
- Access the ResumeMatch web application.
- Upload a resume in PDF format.
- Analyse a resume against a job description.
- View skill matching and similarity results.
- Explore the resume analysis functionality.

---

## ✨ Key Features

### 📄 Resume Processing
- Upload resumes in PDF format.
- Extract textual content using PyMuPDF.
- Process extracted resume content for further analysis.

### 🎯 Skill Extraction and Matching
- Identify technical and professional skills.
- Extract relevant skills from resumes and job descriptions.
- Compare extracted skills against job requirements.
- Identify matched, missing and additional skills.

### 🤖 Text Similarity Analysis
- TF-IDF vectorization for text representation.
- Cosine similarity to measure textual similarity.
- Sentence Transformers implementation for semantic similarity experiments.

### 📊 Skill Gap Analysis
- Calculate skill match percentage.
- Display matched and missing skills.
- Identify keyword overlap.
- Generate structured analysis results.

### 📑 Reports and History
- Generate downloadable PDF analysis reports.
- Store previous analysis records using SQLite.
- View previous analysis results.

---

## 🧠 How ResumeMatch Works

ResumeMatch follows a multi-stage resume analysis pipeline.

```text
       Resume (PDF)          Job Description
             │                      │
             ▼                      ▼
       Text Extraction        Text Processing
             │                      │
             ▼                      ▼
        Resume Text              Job Text
             │                      │
             └──────────┬───────────┘
                        │
                        ▼
                 Skill Extraction
                        │
                        ▼
                 Skill Comparison
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Skill Matching        Text Similarity
                                  │
                           TF-IDF + Cosine
                                  │
             └──────────┬──────────┘
                        │
                        ▼
                  Analysis Results
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
        Skill Gap              PDF Report
         Analysis              Generation
```

### Analysis Workflow

**1. Resume Upload**

The user uploads a resume in PDF format.

**2. Text Extraction**

PyMuPDF extracts textual content from the uploaded resume.

**3. Skill Extraction**

A predefined skill vocabulary and pattern-matching techniques identify relevant skills from the resume and job description.

**4. Skill Matching**

The extracted skills are compared to identify matching, missing and additional skills.

**5. Text Similarity Calculation**

TF-IDF converts text into numerical feature vectors, while cosine similarity measures textual similarity between the resume and job description.

**6. Result Generation**

The application displays skill match percentage, text similarity, keyword overlap and skill gap information.

**7. PDF Report Generation**

The user can download a PDF report containing the analysis results.

**8. Analysis History**

Previous analysis records can be stored and retrieved using SQLite.

---

## 🛠 Technology Stack

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

---

## 🏗 System Architecture

ResumeMatch follows a modular architecture in which different components perform specific tasks.

| Layer | Responsibility |
|---|---|
| Presentation Layer | Resume upload and analysis interface |
| Backend Layer | Application routes and processing |
| PDF Processing Layer | Resume text extraction |
| NLP Layer | Skill extraction and text processing |
| Similarity Layer | TF-IDF and cosine similarity |
| Analysis Layer | Skill comparison and result generation |
| Database Layer | Analysis history management |
| Reporting Layer | PDF report generation |

---

## 📁 Project Structure

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

---

## ⚙️ Installation and Setup

Follow these instructions to run ResumeMatch locally.

### Prerequisites

- Python 3.11 or compatible version
- pip package manager
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kanchann27/ResumeMatch.git
cd ResumeMatch
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000`

---

## ☁️ Deployment

ResumeMatch is deployed using **Render** and connected to the GitHub repository.

### Deployment Configuration

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

### Deployment Considerations

The hosted application uses a lightweight configuration due to the memory limitations of the free hosting environment.

- TF-IDF-based similarity is used for the displayed text similarity score.
- The Sentence Transformers implementation is retained in the codebase but disabled in the hosted environment to reduce memory usage.

---

## 🔬 Technical Approach

### TF-IDF (Term Frequency–Inverse Document Frequency)

TF-IDF converts textual content into numerical vectors based on the importance of words in the documents.

### Cosine Similarity

Cosine similarity measures the similarity between two text vectors.

\[
\text{Cosine Similarity}(A,B)=
\frac{A\cdot B}{\|A\|\|B\|}
\]

### Sentence Transformers

Sentence Transformers are implemented in the project to explore semantic similarity between resume and job description text. This implementation is not enabled in the current hosted configuration.

---

## 🔮 Future Scope

- Support for additional resume formats, including DOCX.
- Improve skill extraction using advanced NLP techniques.
- Integrate semantic similarity into the hosted application.
- Enhance skill recommendations based on missing job requirements.
- Improve the user interface and user experience.
- Introduce more detailed candidate evaluation metrics.
- Explore integration with external job portals.

---

## 👥 The Team

ResumeMatch was developed collaboratively by the following team members:

| Team Member | Institution |
|---|---|
| **Kanchan Chauhan** | Maharishi University of Information Technology |
| **Bhoomi Mahto** | Maharishi University of Information Technology |

Both team members contributed collaboratively to the development of the ResumeMatch project.

---

## 🎓 Academic Context

| Field | Details |
|---|---|
| Project Name | ResumeMatch |
| Project Category | Artificial Intelligence / Machine Learning |
| Team Name | JobFit |
| Institution | Maharishi University of Information Technology |
| Degree | B.Tech |
| Academic Session | 2023–2027 |

---

## 🤝 Contributing

This project was developed as an academic project. Suggestions and improvements are welcome in the following areas:

- Improving skill extraction accuracy.
- Enhancing resume and job description matching.
- Improving the user interface and user experience.
- Adding support for additional resume formats.
- Enhancing analysis reports and recommendations.
- Optimizing application performance.

---

## 📌 Conclusion

ResumeMatch provides a structured approach to resume and job description analysis.

By combining skill extraction, keyword matching, TF-IDF vectorization and cosine similarity, the application helps candidates understand their alignment with job requirements and identify areas for improvement.

The project demonstrates the practical application of Python, NLP and machine learning techniques in recruitment-related automation.

---

**Built with Python, Flask, NLP and Machine Learning.**

*ResumeMatch – Making resume analysis and job matching more effective.*
