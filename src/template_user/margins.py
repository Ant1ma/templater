from dpnds.libraries import *

def create_margins(output_doc):
    for section in output_doc.sections: 
        section.left_margin = Cm(3) 
        section.right_margin = Cm(1) 
        section.top_margin = Cm(2) 
        section.bottom_margin = Cm(2)
