
import os
import sys
import tempfile
import numpy as np

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_file
)


# ==========================================
# 1. PROJECT PATHS
# ==========================================

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
SRC_FOLDER = os.path.join(PROJECT_FOLDER, "src")

sys.path.insert(0, SRC_FOLDER)


# ==========================================
# 2. IMPORT PROJECT MODULES
# ==========================================

from pdf_extractor import extract_text_from_pdf
from skill_extractor import extract_skills

from tfidf_similarity import calculate_text_similarity
from semantic_similarity import calculate_semantic_similarity

from skill_matching import (
    compare_skills,
    calculate_skill_match_percentage
)

from skill_recommender import recommend_skills

from pdf_report import generate_pdf_report

from database import (
    initialize_database,
    save_analysis,
    get_analysis_history
)


# ==========================================
# 3. FLASK APPLICATION
# ==========================================

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

initialize_database()


# ==========================================
# 4. CONVERT NUMPY VALUES
# ==========================================

def convert_to_python_types(data):

    if isinstance(data, dict):

        return {
            key: convert_to_python_types(value)
            for key, value in data.items()
        }

    elif isinstance(data, (list, tuple)):

        return [
            convert_to_python_types(item)
            for item in data
        ]

    elif isinstance(data, np.ndarray):

        return convert_to_python_types(data.tolist())

    elif isinstance(data, np.generic):

        return data.item()

    return data


# ==========================================
# 5. HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# 6. RESUME ANALYSIS ROUTE
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    resume_file = request.files.get("resume")

    job_description = request.form.get(
        "job_description", ""
    ).strip()

    # Validate uploaded resume

    if not resume_file or resume_file.filename == "":

        return jsonify({
            "error": "Please upload your resume PDF."
        }), 400

    if not resume_file.filename.lower().endswith(".pdf"):

        return jsonify({
            "error": "Please upload a PDF file."
        }), 400

    # Validate job description

    if not job_description:

        return jsonify({
            "error": "Please enter a job description."
        }), 400

    temp_path = None

    try:

        # STEP 1: SAVE PDF TEMPORARILY

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_path = temp_file.name

        resume_file.save(temp_path)


        # STEP 2: EXTRACT RESUME TEXT

        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text.strip():

            return jsonify({
                "error": "No readable text found in the PDF. Please upload a text-based PDF."
            }), 400


        # STEP 3: EXTRACT SKILLS

        resume_skills = extract_skills(resume_text)

        job_skills = extract_skills(job_description)


        # STEP 4: TF-IDF SIMILARITY

        tfidf_score = calculate_text_similarity(
            resume_text,
            job_description
        )


        # STEP 5: SEMANTIC SIMILARITY

        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_description
        )


        # STEP 6: COMBINED SIMILARITY

        if semantic_score is None:

            # Hosted lightweight mode: use TF-IDF only

            combined_score = round(
                float(tfidf_score), 2
            )

        else:

            # Full local mode: combine both scores

            combined_score = round(
                (
                    float(tfidf_score)
                    + float(semantic_score)
                ) / 2,
                2
            )


        # STEP 7: SKILL GAP ANALYSIS

        matching, missing, extra = compare_skills(
            resume_skills,
            job_skills
        )


        # STEP 8: SKILL MATCH PERCENTAGE

        skill_percentage = calculate_skill_match_percentage(
            resume_skills,
            job_skills
        )


        # STEP 9: SKILL RECOMMENDATIONS

        recommendations = recommend_skills(missing)


        # STEP 10: PREPARE RESULTS

        results = {

            "resume_skills": resume_skills,

            "job_skills": job_skills,

            "tfidf_similarity": round(
                float(tfidf_score), 2
            ),

            "semantic_similarity": (
                round(float(semantic_score), 2)
                if semantic_score is not None
                else None
            ),

            "combined_text_similarity": round(
                float(combined_score), 2
            ),

            "matching_skills": matching,

            "missing_skills": missing,

            "extra_skills": extra,

            "skill_match_percentage": round(
                float(skill_percentage), 2
            ),

            "recommendations": recommendations

        }


        # STEP 11: CONVERT NUMPY VALUES

        clean_results = convert_to_python_types(results)


        # STEP 12: SAVE ANALYSIS IN SQLITE

        save_analysis(
            resume_file.filename,
            job_description,
            clean_results
        )


        # STEP 13: RETURN JSON TO FRONTEND

        return jsonify(clean_results)


    except Exception:

        app.logger.exception("Resume analysis failed")

        return jsonify({
            "error": "An unexpected error occurred during resume analysis."
        }), 500


    finally:

        # DELETE TEMPORARY PDF

        if temp_path and os.path.exists(temp_path):

            os.remove(temp_path)


# ==========================================
# 7. DOWNLOAD ANALYSIS REPORT
# ==========================================

@app.route("/download-report", methods=["POST"])
def download_report():

    try:

        data = request.get_json(silent=True) or {}

        resume_filename = data.get(
            "resume_filename",
            "Resume.pdf"
        )

        results = data.get("results")

        if not isinstance(results, dict):

            return jsonify({
                "error": "Invalid report data."
            }), 400

        pdf_buffer = generate_pdf_report(
            resume_filename,
            results
        )

        return send_file(
            pdf_buffer,
            mimetype="application/pdf",
            as_attachment=True,
            download_name="ResumeMatch_Analysis_Report.pdf"
        )

    except Exception:

        app.logger.exception("PDF report generation failed")

        return jsonify({
            "error": "Unable to generate the PDF report."
        }), 500


# ==========================================
# 8. ANALYSIS HISTORY PAGE
# ==========================================

@app.route("/history")
def history():

    try:

        records = get_analysis_history()

        return render_template(
            "history.html",
            records=records
        )

    except Exception:

        app.logger.exception("Unable to retrieve analysis history")

        return "Unable to load analysis history.", 500


# ==========================================
# 9. FILE SIZE ERROR HANDLER
# ==========================================

@app.errorhandler(413)
def file_too_large(error):

    return jsonify({
        "error": "File is too large. Maximum allowed size is 10 MB."
    }), 413


# ==========================================
# 10. PAGE NOT FOUND HANDLER
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return "Page not found.", 404


# ==========================================
# 11. RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
