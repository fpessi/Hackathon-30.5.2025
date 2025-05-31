# This object compiles a docx format report from user input
# Uses python-docx library

from docx import Document
from docx.shared import Pt, RGBColor
import os
import sys

def get_output_directory():
    """Ensure the output directory exists and return its path."""
    if '__file__' in globals():
        base_path = os.path.dirname(__file__)
    else:
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Define relative path and create it if it doesn't exist
    relative_path = os.path.join(base_path, "..", "Case")
    os.makedirs(relative_path, exist_ok=True)
    return relative_path

def make_report():
    doc = Document()

    # Title
    title = doc.add_paragraph()
    run = title.add_run('Technical Field Report')
    font = run.font
    font.name = 'Calibri'
    font.size = Pt(28)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)

    # General Information Header
    general_header = doc.add_paragraph()
    run2 = general_header.add_run('General Information')
    font2 = run2.font
    font2.name = 'Calibri'
    font2.size = Pt(20)
    font2.bold = True
    font2.color.rgb = RGBColor(0, 0, 0)

    # Table 1: General Info
    table1 = doc.add_table(rows=5, cols=2)
    table1.style = 'Table Grid'
    general_info = ["Location", "Date", "Service personnel", "Equipment", "Time of service"]
    general_answer = ["", "", "", "", ""]  # Placeholder or user input
    for i, label in enumerate(general_info):
        cell_left = table1.cell(i, 0)
        cell_left.text = label
        run_left = cell_left.paragraphs[0].runs[0]
        run_left.font.name = 'Calibri'
        run_left.font.size = Pt(14)
    for i, value in enumerate(general_answer):
        cell_right = table1.cell(i, 1)
        cell_right.text = value
        run_right = cell_right.paragraphs[0].runs[0]
        run_right.font.name = 'Calibri'
        run_right.font.size = Pt(14)

    # Field Work Header
    field_header = doc.add_paragraph()
    run3 = field_header.add_run('Field Work Description')
    font3 = run3.font
    font3.name = 'Calibri'
    font3.size = Pt(20)
    font3.bold = True
    font3.color.rgb = RGBColor(0, 0, 0)

    # Table 2: Field Work
    table2 = doc.add_table(rows=4, cols=2)
    table2.style = 'Table Grid'
    description_info = ["Reason of service", "Work description", "Problems with service", "Notes"]
    description_answer = ["", "", "", ""]  # Placeholder
    for i, label in enumerate(description_info):
        cell_left = table2.cell(i, 0)
        cell_left.text = label
        run_left = cell_left.paragraphs[0].runs[0]
        run_left.font.name = 'Calibri'
        run_left.font.size = Pt(14)
    for i, value in enumerate(description_answer):
        cell_right = table2.cell(i, 1)
        cell_right.text = value
        run_right = cell_right.paragraphs[0].runs[0]
        run_right.font.name = 'Calibri'
        run_right.font.size = Pt(14)

    # Supply Info Header
    supply_header = doc.add_paragraph()
    run4 = supply_header.add_run('Detailed Supply Information')
    font4 = run4.font
    font4.name = 'Calibri'
    font4.size = Pt(20)
    font4.bold = True
    font4.color.rgb = RGBColor(0, 0, 0)

    # Table 3: Supply Info
    table3 = doc.add_table(rows=4, cols=2)
    table3.style = 'Table Grid'
    field_info = ["Supplies and amounts", "Weight", "Length", "Width"]
    field_answer = ["", "", "", ""]  # Placeholder
    for i, label in enumerate(field_info):
        cell_left = table3.cell(i, 0)
        cell_left.text = label
        run_left = cell_left.paragraphs[0].runs[0]
        run_left.font.name = 'Calibri'
        run_left.font.size = Pt(14)
    for i, value in enumerate(field_answer):
        cell_right = table3.cell(i, 1)
        cell_right.text = value
        run_right = cell_right.paragraphs[0].runs[0]
        run_right.font.name = 'Calibri'
        run_right.font.size = Pt(14)

    # Special Info Header
    special_header = doc.add_paragraph()
    run5 = special_header.add_run('Special Information')
    font5 = run5.font
    font5.name = 'Calibri'
    font5.size = Pt(20)
    font5.bold = True
    font5.color.rgb = RGBColor(0, 0, 0)

    # Table 4: Special Info
    table4 = doc.add_table(rows=1, cols=1)
    table4.style = 'Table Grid'
    special_information_answer = [""]  # Placeholder
    for i, value in enumerate(special_information_answer):
        cell = table4.cell(i, 0)
        cell.text = value
        run = cell.paragraphs[0].runs[0]
        run.font.name = 'Calibri'
        run.font.size = Pt(14)

    # Save the document
    output_dir = get_output_directory()
    output_path = os.path.join(output_dir, "field_report.docx")
    doc.save(output_path)
    print(f"Report saved to: {output_path}")

if __name__ == "__main__":
    make_report()

