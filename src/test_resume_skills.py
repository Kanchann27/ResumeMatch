
from pathlib import Path

from pdf_extractor import extract_text_from_pdf
from skill_extractor import extract_skills


project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "data"

pdf_files = list(data_folder.glob("*.pdf"))

if len(pdf_files) == 1:

    resume_text = extract_text_from_pdf(pdf_files[0])

    skills = extract_skills(resume_text)

    print("\nUPDATED RESUME SKILLS")
    print("=====================")

    for skill in skills:
        print("-", skill)

else:
    print("Please keep exactly one PDF in the data folder.")
