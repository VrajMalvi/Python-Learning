# link : https://pypi.org/project/PyPDF2/
# documentation : https://pythonhosted.org/PyPDF2/

import PyPDF2

# with out 'rb' more it cant read pdf

# with open('17_Scripting-with-python/2_pdf-with-python/dummy.pdf', 'rb') as file:
#     # print(file)
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     # print(reader.getPage(0))  # prints page object of first page(0)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('17_Scripting-with-python/2_pdf-with-python/tilt.pdf', 'wb') as newfile:
#         writer.write(newfile)


# ----------------------------------------------------------------------------------------------------
# pdf merge program
# NOTE to run code type: python 17_Scripting-with-python/2_pdf-with-python/pdf.py dummy.pdf twopage.pdf wtr.pdf

# import sys

# inputs = sys.argv[1:]  # will grab all args accept file name

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(f'17_Scripting-with-python/2_pdf-with-python/{pdf}')
#     merger.write('17_Scripting-with-python/2_pdf-with-python/super.pdf')


# pdf_combiner(inputs)


# ---------------------------------------------------------------
# program to watermark pdfs

template = PyPDF2.PdfFileReader(
    open('17_Scripting-with-python/2_pdf-with-python/super.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(
    open('17_Scripting-with-python/2_pdf-with-python/wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('17_Scripting-with-python/2_pdf-with-python/water_mark.pdf', 'wb') as file:
        output.write(file)
