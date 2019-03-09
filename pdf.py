import PyPDF2
import re
import sys
from degree import get_courses, get_dict

def main(file_name):
    d = {}
    # creating a pdf file object
    pdfFileObj = open(file_name, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    if pdfReader.isEncrypted:
        print("please first decrypted the file by export it to a plain pdf or using qpdf")
        exit(1)

    pageObj = pdfReader.getPage(0)

    # extracting text from page
    txt = pageObj.extractText()
    terms = txt.split('Undergraduate EngineeringGradeHoursMSHCTPMHP')
    pattern = '[A-Z]{4,}[  ][0-9]{3}'
    cleaner = re.compile(pattern)
    all_courses = []
    for term in terms[2:]:
        courses = cleaner.findall(term)
        all_courses += [course.replace(' ','') for course in courses]
    print('courses you have taken: \n', all_courses)

    # closing the pdf file object
    pdfFileObj.close()

    get_dict()
    get_courses(all_courses)

if __name__ =='__main__':
    if len(sys.argv) != 2:
        print('usage: python pdf.py <file>')
        exit(1)
    main(sys.argv[1])
