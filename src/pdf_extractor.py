
import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path):

    document = pymupdf.open(pdf_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text


if __name__ == "__main__":

    project_folder = Path(__file__).resolve().parent.parent
    data_folder = project_folder / "data"

    pdf_files = list(data_folder.glob("*.pdf"))

    if len(pdf_files) == 0:
        print("No PDF resume found.")

    elif len(pdf_files) > 1:
        print("Multiple PDF files found.")

    else:
        pdf_path = pdf_files[0]

        print("Reading resume:", pdf_path.name)

        resume_text = extract_text_from_pdf(pdf_path)

        print("\nEXTRACTED RESUME TEXT")
        print(resume_text)
