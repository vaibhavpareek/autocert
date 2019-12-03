from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import csv
reg = input("Enter the CSV file location : ")
print("\n")
X = int(input("Enter the X Coordinate : "))
print("\n")
Y = int(input("Enter the Y Coordinate : "))
reader = csv.DictReader(open(reg))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
j = 0
cert = input("Enter the Certificate Location with Name : ")
for i in reader:
	if(i['Name']!=""):
		packet = io.BytesIO()
		# create a new PDF with Reportlab
		can = canvas.Canvas(packet, pagesize=letter)
		can.setFont("Vera",20)
		can.drawString(X, Y, i['Name'])#363,210
		can.save()
		#move to the beginning of the StringIO buffer
		packet.seek(0)
		new_pdf = PdfFileReader(packet)
		# read your existing PDF
		email = i['Username']+".pdf"
		existing_pdf = PdfFileReader(open(cert, "rb"))
		output = PdfFileWriter()
		# add the "watermark" (which is the new pdf) on the existing page
		page = existing_pdf.getPage(0)
		page.mergePage(new_pdf.getPage(0))
		output.addPage(page)
		# finally, write "output" to a real file
		outputStream = open(email, "wb")
		output.write(outputStream)
		outputStream.close()
		j = j+1
		print("Certificate Done : "+str(j))