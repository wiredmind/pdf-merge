from PyPDF2 import PdfFileReader, PdfFileWriter
from time import sleep
import sys
import os
import msvcrt

print(
    'Choose the type of the document you are creating\n'
    '(1) Inspection\n'
    '(2) Right of Entry\n'
    '(3) Other\n'
    '\n'
    '>>>', end=" "
    )

while True:
    type = msvcrt.getch()
    if type == b'1':        
        suffix = 'INSPECTION'
        break
    elif type == b'2':
        suffix = "RIGHT OF ENTRY"
        break
    elif type == b'3':
        suffix = "OTHER"
        break
os.system('cls')

if suffix == 'OTHER':
    print(
        '# Selected document type: {}\n'
        '# File name will not be appened.\n'
        .format(suffix)
        )
else:
    print(
        '# Selected document type: {}\n'
        '# File name will be appened with _{}\n'
        .format(suffix, suffix))

fileName = input('Enter file name (and press Enter): ')

try:
    root = os.path.split(sys.argv[1])[0]
    fileName = fileName.upper() + '_' + suffix + '.pdf'
    destination = os.path.join(root, fileName)
except IndexError:
    os.system('color 0C')
    print("# Error: No files received for processing.")
    sleep(3)
    os.system('color 07')
    exit()

fileList = sys.argv[1:]
fileList.sort()

outFile = PdfFileWriter()
outStream = file(destination, 'wb')

for item in fileList:
    pdfFile = file(item, 'rb')
    outFile.addPage(
        PdfFileReader(pdfFile).getPage(0))
    outFile.write(outStream)
    pdfFile.close()
    os.remove(item)

outStream.close()