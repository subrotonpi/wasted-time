#!/usr/bin/env python
# coding: utf-8

# In[10]:
#before this
#create a list/excel of students/guardians
#using main-merge in msword create a doc, convert to pdf
#then use this code

# pdf_splitter.py

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd
df = pd.read_excel('letters/info.xlsx', index_col=0)  

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        output_filename = 'ID__{}___Guardian___{}___.pdf'.format(
            df['ID (in English)'].values[page], 
            df['বাবা/মা/অভিভাবক এর নাম(বাংলায়)'].values[page]
        )
         
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    path = 'letters/merged.pdf'
    pdf_splitter(path)

