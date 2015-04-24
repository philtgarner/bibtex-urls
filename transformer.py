#!/usr/bin/python

import sys
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding

#The counter to keep track of how many records we've changed
count = 0

#The length of the command line arguments 
length = len(sys.argv)
#If we've got one param use the input to build the output file name
if(length == 2):
	input = sys.argv[1]
	output = input + 'urls.bib'
#If we've got two params use one for input and one for output
elif(length >= 3):
	input = sys.argv[1]
	output = sys.argv[2]
#If no params then exit with a warning
else:
	print('At least one parameter is needed, provide the BibTeX file to parse is required')
	sys.exit(0)
	
#Open the database 
with open(input, encoding="utf-8") as bibtex_file:
	parser = BibTexParser()
	parser.customization = homogeneize_latex_encoding
	bib_database = bibtexparser.load(bibtex_file, parser=parser)
	
	#Loop through the entries in the BibTeX database
	for e in bib_database.entries:
		#If the entry is clasified as 'misc' then look to edit it
		if(e['type'] == 'misc'):
			#If there is a link and no howpublished component then we can edit
			if('link' in e and 'howpublished' not in e):
				url = e['link']
				howpublished = '\\url{' + url + '}'
				e['howpublished'] = howpublished
				count += 1

#Open the output database and write the modified database
with open(output, 'w', encoding="utf-8") as bibtex_output:
	bibtexparser.dump(bib_database, bibtex_output)

#Print some info for the user
print(input + ' --> ' + output)
print('Converted ' + str(count) + ' entries')
