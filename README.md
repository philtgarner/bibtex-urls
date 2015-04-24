# bibtex-urls
A [Python](https://www.python.org/) script to add the howpublished field to the misc entries that have a URL field.

##Mendeley
[Mendeley](https://www.mendeley.com/) is a reference manager that has the capability to export the references to a BibTeX file.

A common problem with this exported file is that the URLs aren't displayed in the bibliography correctly, Mendeley places links in the `url` field whereas they need to be in the `howpublished` field. This script will add the attribute to the file where appropriate.

##How to run
The program requires two arguments, the input and the output file:
```
transformer.py input.bib output.bib
```

##Using the file
When using the `listings` package I had the problem of the citations not being compiled properly. Solve this by using `\usepackage{textcomp}`.

##bibtexparser
This script uses [bibtexparser](https://pypi.python.org/pypi/bibtexparser/) and this should be installed for this script to run.

##Disclaimer
I am neither a Python nor a BibTeX expert so any suggestions or improvements to this code are more than welcome.
