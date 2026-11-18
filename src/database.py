
import sqlite3
import json
from pathlib import Path
from datetime import datetime


# ==========================================
# 1. DATABASE PATH
# ==========================================

PROJECT_FOLDER = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_FOLDER / "data"

DATA_FOLDER.mkdir(exist_ok=True)

DATABASE_PATH = DATA_FOLDER / "resume_match.db"


# ==========================================
# 2. DATABASE CONNECTION
# ==========================================

def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection


# ==========================================
# 3. INITIALIZE DATABASE
# ==========================================

def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_filename TEXT NOT NULL,

            job_description TEXT NOT NULL,

            tfidf_similarity REAL,

            semantic_similarity REAL,

            combined_similarity REAL,

            skill_match_percentage REAL,

            matching_skills TEXT,

            missing_skills TEXT,

            extra_skills TEXT,

            recommendations TEXT,

            analysis_date TEXT

        )
    """)

    connection.commit()

    connection.close()

    print("Database initialized successfully!")


# ==========================================
# 4. SAVE ANALYSIS
# ==========================================

def save_analysis(resume_filename, job_description, results):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (

            resume_filename,
            job_description,
            tfidf_similarity,
            semantic_similarity,
            combined_similarity,
            skill_match_percentage,
            matching_skills,
            missing_skills,
            extra_skills,
            recommendations,
            analysis_date

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        resume_filename,

        job_description,

        results["tfidf_similarity"],

        results["semantic_similarity"],

        results["combined_text_similarity"],

        results["skill_match_percentage"],

        json.dumps(results["matching_skills"]),

        json.dumps(results["missing_skills"]),

        json.dumps(results["extra_skills"]),

        json.dumps(results["recommendations"]),

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    connection.commit()

    connection.close()

    print("Analysis saved successfully!")


# ==========================================
# 5. RETRIEVE ALL ANALYSES
# ==========================================

def get_analysis_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM analyses
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    history = []

    for record in records:

        analysis = dict(record)

        analysis["matching_skills"] = json.loads(
            analysis["matching_skills"]
        )

        analysis["missing_skills"] = json.loads(
            analysis["missing_skills"]
        )

        analysis["extra_skills"] = json.loads(
            analysis["extra_skills"]
        )

        analysis["recommendations"] = json.loads(
            analysis["recommendations"]
        )

        history.append(analysis)

    return history


# ==========================================
# 6. TEST DATABASE MODULE
# ==========================================

if __name__ == "__main__":

    initialize_database()

    saved_records = get_analysis_history()

    print("\n========== ANALYSIS HISTORY ==========")

    for record in saved_records:

        print("\nAnalysis ID:", record["id"])

        print("Resume:", record["resume_filename"])

        print(
            "Skill Match:",
            record["skill_match_percentage"],
            "%"
        )

        print("Date:", record["analysis_date"])
