from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(content):
    filename = "Travel_Plan.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)

    return filename