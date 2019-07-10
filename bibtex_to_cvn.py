"""
@author		: Jorge Lillo-Box
Goal		: Bibtex cleaner for CVN
Description	: Change the ADS bibliographic style to one acceptable by CVN. Changes 
			  include accents, journal names, removal of "{" and "}"
Version date: 17.nov.2016
Dependencies: bibtexparser, numpy, sys
Intructions	: 
	1. Go to ADS and mark all references that you want to be included (e.g., your personal
	   bibliography).
	2. Scroll down to "Retrieve the above records in other formats or sort order".
	3. In the field "Return", select "BibTeX reference list"
	4. In the next field select "Save to file".
	5. In the same folfer as where you save this file and this routine, run:
			python bibtex_to_cvn.py [filename.bbl]
	6. The output will be a file named:  "[filename]_cleaned4cvn.bib"
	7. Import this file at CVN as BibTeX
"""

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import numpy as np
import sys
import argparse

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help=".bib file to be cleaned and converted to CVN")
    args = parser.parse_args()
    return args


def remove_multiple_strings(cur_string, replace_list):
	for cur_word in replace_list:
		cur_string = cur_string.replace(cur_word, "")
		#print cur_string
	return cur_string

if __name__ == "__main__":

	print '---------------------------------'
	print '      Bibtex cleaner for CVN     '
	print '        (by  J. Lillo-Box)       '
	print '---------------------------------'
	args = cli()
	file = args.file

	with open(file) as bibtex_file:
		 bibtex_str = bibtex_file.read()

	bib = bibtexparser.loads(bibtex_str)
	npapers = len(bib.entries)


	a = np.genfromtxt('journals.lis',delimiter=',',dtype='string',autostrip=True)
	abb = a[:,0]
	journal = a[:,1]

	count=0
	for paper in bib.entries:
	
		#print paper["author"]
		paper["author"] = remove_multiple_strings(paper["author"],["{","}"])
		paper["author"] = paper["author"].replace("~"," ")
		paper["author"] = paper["author"].replace(" and\n","; ")

		#paper["author"] = paper["author"].replace(" and ","; ")
	
		paper["author"] = paper["author"].replace('\\"a',"a")
		paper["author"] = paper["author"].replace('\\"e',"e")
		paper["author"] = paper["author"].replace('\\"i',"i")
		paper["author"] = paper["author"].replace('\\"o',"o")
		paper["author"] = paper["author"].replace('\\"u',"u")

		paper["author"] = paper["author"].replace("\\'\a","a")
		paper["author"] = paper["author"].replace("\\'\e","e")
		paper["author"] = paper["author"].replace("\\'\i","i")
		paper["author"] = paper["author"].replace("\\'\o","o")
		paper["author"] = paper["author"].replace("\\'\u","u")

		paper["author"] = paper["author"].replace("\\'u","u")
		paper["author"] = paper["author"].replace("\\'e","e")
		paper["author"] = paper["author"].replace("\\'a","a")
		paper["author"] = paper["author"].replace("\\'i","i")
		paper["author"] = paper["author"].replace("\\'o","o")
		paper["author"] = paper["author"].replace("\\'u","u")

		paper["author"] = paper["author"].replace("\\`u","u")
		paper["author"] = paper["author"].replace("\\`e","e")
		paper["author"] = paper["author"].replace("\\`a","a")
		paper["author"] = paper["author"].replace("\\`i","i")
		paper["author"] = paper["author"].replace("\\`o","o")
		paper["author"] = paper["author"].replace("\\`u","u")
	
		paper["author"] = paper["author"].replace("\\~u","u")
		paper["author"] = paper["author"].replace("\\~e","e")
		paper["author"] = paper["author"].replace("\\~a","a")
		paper["author"] = paper["author"].replace("\\~i","i")
		paper["author"] = paper["author"].replace("\\~o","o")
		paper["author"] = paper["author"].replace("\\~u","u")

	
		try:
			paper["journal"] = journal[np.where(abb == paper["journal"][1:])[0]][0]
		except:
			tmp=0

		#\in
	
		count = count+1

	print "Number of papers processed:",len(bib.entries)

	writer = BibTexWriter()
	writer.indent = '    '     # indent entries with 4 spaces instead of one
	_tmp = file.split('.')
	new_file_name = _tmp[0]+'_cleaned4cvn.bib'
	with open(new_file_name, 'w') as bibfile:
		bibfile.write(writer.write(bib))