"""
pip install tk
pip install ghostscript
pip install camelot-py
"""

import camelot 
import ghostscript

tables = camelot.read_pdf('data/foo.pdf', pages='1', flavor='lattice')
print(tables)

tables.export('data/foo.csv', f='csv', compress=True)
tables[0].to_csv('data/foo.csv')  # to a csv file
print(tables[0].df)  # to a df