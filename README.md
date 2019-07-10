# bibtex_to_cvn
 Bibliography converter to CVN format

@author        : Jorge Lillo-Box

Goal        : Bibtex cleaner for CVN

Description    : Change the ADS bibliographic style to one acceptable by CVN. Changes 
include accents, journal names, removal of "{" and "}"

Version date: 17.nov.2016

Dependencies: bibtexparser, numpy, sys

*Intructions    : 

    1. Go to ADS and mark all references that you want to be included (e.g., your personal
       bibliography).

    2. Scroll down to "Retrieve the above records in other formats or sort order".

    3. In the field "Return", select "BibTeX reference list"

    4. In the next field select "Save to file".

    5. In the same folfer as where you save this file and this routine, run:
            python bibtex_to_cvn.py [filename.bbl]

    6. The output will be a file named:  "[filename]_cleaned4cvn.bib"

    7. Import this file at CVN as BibTeX
