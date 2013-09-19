import sys
import os
import msvcrt
from PyPDF2 import PdfFileReader, PdfFileWriter

print 'Choose the type of the document you are creating'
sys.stdout.write('(1) Inspection\n(2) Right of Entry\n(3) Other\n\n>>> ')

while True:
    type = msvcrt.getch()
    if type == chr(49):        
        suffix = 'INSPECTION'
        break
    elif type == chr(50):
        suffix = "RIGHT OF ENTRY"
        break
    elif type == chr(51):
        suffix = "OTHER"
        break
os.system('cls')

if suffix == 'OTHER':
    print """# Selected document type: {}
# File name will not be appened.
""".format(suffix)
else:
    print """# Selected document type: {}
# File name will be appened with _{}
""".format(suffix, suffix)

fileName = raw_input('Enter file name (and press Enter): ')

root = os.path.split(sys.argv[1])[0]
fileName = fileName.upper() + '_' + suffix + '.pdf'
destination = os.path.join(root, fileName)

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
