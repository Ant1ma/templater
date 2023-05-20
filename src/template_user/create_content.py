from dpnds.libraries import *

def create_content(input_doc, output_doc, name_docx):
    doci = output_doc 
    count = 0 
    counter = 0 

    for para in input_doc.paragraphs: 
        if 'Рисунок' in para.text: 
            count += 1 
            pic_ins = doci.add_picture(f'pic_{name_docx}/word/media/image{count}.png', width=Cm(16), height=Cm(10)) 
            pic_ins.alignment = WD_ALIGN_PARAGRAPH.CENTER
        output_para = doci.add_paragraph() 
        for run in para.runs: 
            output_run = output_para.add_run(run.text) 
            output_run.font.name = 'Times New Roman' 
            if run.bold:
                counter += 1 
                naming = f'Bookmark {counter}' 
                tag = output_doc.element.xpath('//w:p')[-1]

                start_b = OxmlElement('w:bookmarkStart')
                start_b.set(qn('w:id'), f'{counter}')
                start_b.set(qn('w:name'), para.text)
                tag.append(start_b)
                
#                text_b = OxmlElement('w:r')
#                text_b.text = para.text
#                tag.append(text_b)
                output_run.bold = True
                
                end_b = OxmlElement('w:bookmarkEnd')
                end_b.set(qn('w:id'), f'{counter}')
                end_b.set(qn('w:name'), para.text)
                tag.append(end_b)
                #output_run.add_bookmark(naming)

            output_run.italic = run.italic 
            output_run.underline = run.underline 
            output_run.font.color.rgb = run.font.color.rgb 
            output_run.font.name = run.font.name   
            if 'Рисунок' in para.text:
                output_run.font.size = Pt(12) 
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER 
            elif 'Таблица' in para.text: 
                output_run.font.size = Pt(12) 
                para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            else: 
                output_run.font.size = Pt(14) 
                output_para.paragraph_format.alignment = para.paragraph_format.alignment

