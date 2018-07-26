# Read & Edit PDFs

import PyPDF2
import os

print("This module will use the PyPDF2 & os modules")

os.chdir('c:\\users\\drew\\downloads\\auto')

pdfFile = open('meetingminutes2.pdf', 'rb')
print("pdf's need to be in read binary file type. THat's why we'll put pdfFile = open('meetingminutes2.pdf', 'rb')")

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())

#This will print all of the text
#for pageNum in range(reader.numPages):
#   print(reader.getPage(pageNum).extractText())

pdfFileOrig = open('meetingminutes.pdf', 'rb')
readerOrig = PyPDF2.PdfFileReader(pdfFileOrig)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(readerOrig.numPages):
    page = readerOrig.getPage(pageNum)
    writer.addPage(page)

# wb = write binary
outputFile = open('combinedMinutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFileOrig.close()
