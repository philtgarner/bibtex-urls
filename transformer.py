#!/usr/bin/python

import sys
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
import datetime

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
	
#Open the database - no special encoding needed, we can assume that Mendeley has produced a clean BibTeX file
with open(input, encoding="utf-8") as bibtex_file:
	parser = BibTexParser()
	bib_database = bibtexparser.load(bibtex_file, parser=parser)
	
	#Loop through the entries in the BibTeX database
	for e in bib_database.entries:
		#If we have a title (should always be the case but check just in case) then make sure the title is in braces to maintain any capitalisation
		if('title' in e):
			e['title'] = '{' + e['title'] + '}'
		#If the entry is clasified as 'misc' then look to edit it
		if(e['type'] == 'misc'):
			#If there is a link and no howpublished component then we can edit
			if('link' in e and 'howpublished' not in e):
				#Remove any back slashes, there is no need to escape characters, they 
				url = e['link'].replace('\\', '')
				howpublished = '\\url{' + url + '}'
				e['howpublished'] = howpublished
				count += 1
			#If there is an author (there always should be) then make sure the capitalisation is preserved for misc entries
			if('author' in e and ',' not in e['author']):
				e['author'] = '{' + e['author'] + '}'
			#If there is a URL date then add this as a note so it'll appear in the references
			if('urldate' in e):
				#We assume the date is in the format yyyy-mm-dd (as used by Mendeley
				dateSplit = e['urldate'].split('-')
				#Get the components of the date and format them nicely for the output
				if(len(dateSplit) == 3):
					date = datetime.date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
					note = date.strftime('Accessed: %d %b %Y')
					e['note'] = note

#Open the output database and write the modified database
with open(output, 'w', encoding="utf-8") as bibtex_output:
	bibtexparser.dump(bib_database, bibtex_output)

#Print some info for the user
print(input + ' --> ' + output)
print('Converted ' + str(count) + ' entries')
