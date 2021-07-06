import PyPDF2 
 
pdf1File = open('D:\\College Files\\Internship\\bootcamp\\python\\d22\\1file.pdf', 'rb')
pdf2File = open('D:\\College Files\\Internship\\bootcamp\\python\\d22\\2file.pdf', 'rb')
 
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()
 

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

pdf3 = open("MergedFiles.pdf",'rb')
pdf3Reader = PyPDF2.PdfFileReader(pdf3)

print(pdf3Reader)
