# This object compiles a docx format report from user input
# Uses python-docx library
from docx import Document
from docx.shared import Pt, RGBColor
class Reporter(object):

  def __init__(self):
    pass

doc = Document()

title = doc.add_paragraph()
run = title.add_run('Technical Field Report')
font = run.font
font.name = 'Calibri'
font.size = Pt(28)
font.bold = True
font.color.rgb = RGBColor(0, 0, 0)


general_header = doc.add_paragraph()
run2 = general_header.add_run('General Information')
font2 = run2.font
font2.name = 'Calibri'
font2.size = Pt(20)
font2.bold = True
font2.color.rgb = RGBColor(0, 0, 0)

#Taulukko 1
table1 = doc.add_table(rows=5, cols=2)
table1.style = 'Table Grid'
general_info = ["Location", "Date", "Service personnel", "Area of service", "Time of service"]
general_answer=[]
for i, label in enumerate(general_info):
    cell_left = table1.cell(i, 0)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)
for i, label in enumerate(general_answer):
    cell_left = table1.cell(i, 1)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)



field_header = doc.add_paragraph()
run3 = field_header.add_run('Field Work Description')
font3 = run3.font
font3.name = 'Calibri'
font3.size = Pt(20)
font3.bold = True
font3.color.rgb = RGBColor(0, 0, 0)

#Taulukko 2
table2 = doc.add_table(rows=4, cols=2)
table2.style = 'Table Grid'
description_info = ["Reason of service", "Work description", "Problems with service", "Notes"]
description_answer=[]
for i, label in enumerate(description_info):
    cell_left = table2.cell(i, 0)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)
for i, label in enumerate(description_answer):
    cell_left = table2.cell(i, 1)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)


supply_header = doc.add_paragraph()
run4 = supply_header.add_run('Detailed Supply Information')
font4 = run4.font
font4.name = 'Calibri'
font4.size = Pt(20)
font4.bold = True
font4.color.rgb = RGBColor(0, 0, 0)

#Taulukko 3
table3 = doc.add_table(rows=4, cols=2)
table3.style = 'Table Grid'
field_info = ["Supplies and amounts", "Weight", "Length", "Width"]
field_answer=[]
for i, label in enumerate(field_info):
    cell_left = table3.cell(i, 0)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)
for i, label in enumerate(field_answer):
    cell_left = table3.cell(i, 1)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)

field_header = doc.add_paragraph()
run5 = field_header.add_run('Special information ')
font5 = run5.font
font5.name = 'Calibri'
font5.size = Pt(20)
font5.bold = True
font5.color.rgb = RGBColor(0, 0, 0)


table4 = doc.add_table(rows=1, cols=1)
table4.style = 'Table Grid'
special_information_answer=[]
for i, label in enumerate(special_information_answer):
    cell_left = table4.cell(i, 0)
    paragraph_left = cell_left.paragraphs[0]
    paragraph_left.clear()
    run_left = paragraph_left.add_run(label)
    run_left.font.name = 'Calibri'
    run_left.font.size = Pt(14)


# Tallenna dokumentti
doc.save("formatted_field_report.docx")
