from dpnds.libraries import *

def create_lists(input_doc, output_doc): 
    for paragraph in input_doc.paragraphs: 
        for run in paragraph.runs: 
            if run.bold and paragraph.text != '':
                list_count = output_doc.add_paragraph( style='List Number').add_run(f'{paragraph.text}') 
                list_count.bold = True 
                list_count.font.name = 'Times New Roman' 
                list_count.font.size = Pt(14)
    output_doc.add_page_break()
 
