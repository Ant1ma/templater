from dpnds.libraries import *

def extract_pictures(name_of_file): 
    doc_for_ex = f'./docx_files/{name_of_file}' 
    docx = doc_for_ex 
    ex_dir = pathlib.Path(f'pic_{name_of_file}') 

    if not ex_dir.is_dir():
	    ex_dir.mkdir() 
	    with zipfile.ZipFile(docx) as zf: 
		    for name in zf.infolist(): 
			    zf.extract(name, ex_dir) 

