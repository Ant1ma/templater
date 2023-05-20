from dpnds.dependes import *
from dpnds.libraries import *

def create_document(doc, naming):
    extract_pictures(naming) 
    doci = Document() 
    create_margins(doci) 
    create_lists(doc, doci) 
    create_content(doc, doci, naming) 
    doci.save(f'result.docx')

if __name__ == "__main__": 
    docx = 'OST-1st.docx' 
    doc = Document(f'./docx_files/{docx}') 
    create_document(doc, docx)