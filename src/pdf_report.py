
from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)


def generate_pdf_report(resume_filename, results):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        fontSize=22,
        leading=28,
        textColor=colors.HexColor("#173B75"),
        alignment=TA_CENTER,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name="SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=colors.HexColor("#173B75"),
        spaceBefore=14,
        spaceAfter=8
    ))

    story = []

    # Report title
    story.append(Paragraph("ResumeMatch", styles["ReportTitle"]))
    story.append(Paragraph(
        "Resume–Job Matching Analysis Report",
        styles["Normal"]
    ))
    story.append(Spacer(1, 12))

    # Basic information
    story.append(Paragraph(
        f"<b>Resume:</b> {resume_filename}",
        styles["Normal"]
    ))

    story.append(Paragraph(
        f"<b>Report generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        styles["Normal"]
    ))

    story.append(HRFlowable(
        width="100%",
        color=colors.HexColor("#DCE3EF"),
        spaceBefore=10,
        spaceAfter=10
    ))

    # Similarity scores
    story.append(Paragraph(
        "1. Similarity Scores",
        styles["SectionHeading"]
    ))

    semantic_score = results.get("semantic_similarity")

    semantic_display = (
        f"{semantic_score}%"
        if semantic_score is not None
        else "N/A (Unavailable in lightweight deployment)"
    )

    score_data = [
        ["Metric", "Score"],
        ["Skill Match", f"{results.get('skill_match_percentage', 0)}%"],
        ["TF-IDF Similarity", f"{results.get('tfidf_similarity', 0)}%"],
        ["Semantic Similarity", semantic_display],
        ["Combined Text Similarity", f"{results.get('combined_text_similarity', 0)}%"]
    ]

    score_table = Table(
        score_data,
        colWidths=[100 * mm, 55 * mm]
    )

    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#173B75")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DCE3EF")),
        ("PADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    ]))

    story.append(score_table)

    # Skill lists
    skill_sections = [
        ("2. Matching Skills", "matching_skills"),
        ("3. Missing Skills", "missing_skills"),
        ("4. Additional Skills", "extra_skills")
    ]

    for heading, key in skill_sections:

        story.append(Paragraph(
            heading,
            styles["SectionHeading"]
        ))

        skills = results.get(key, [])

        if skills:
            for skill in sorted(skills):
                story.append(Paragraph(
                    f"• {skill}",
                    styles["Normal"]
                ))
        else:
            story.append(Paragraph(
                "None",
                styles["Normal"]
            ))

    # Recommendations
    story.append(Paragraph(
        "5. Skill Development Recommendations",
        styles["SectionHeading"]
    ))

    recommendations = results.get("recommendations", {})

    if recommendations:

        for skill, tips in recommendations.items():

            story.append(Paragraph(
                f"<b>{skill}</b>",
                styles["Normal"]
            ))

            for tip in tips:
                story.append(Paragraph(
                    f"• {tip}",
                    styles["Normal"]
                ))

            story.append(Spacer(1, 6))

    else:
        story.append(Paragraph(
            "No skill gaps identified.",
            styles["Normal"]
        ))

    story.append(Spacer(1, 20))

    story.append(Paragraph(
        "Note: These scores are analytical indicators, not a guarantee of job selection.",
        styles["Italic"]
    ))

    document.build(story)

    buffer.seek(0)

    return buffer
