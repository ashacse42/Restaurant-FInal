import fpdf

data=[1,2,3,4,5,6]

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

for i in data:
    pdf.write(5,str(i))
    pdf.ln()
pdf.output("testings.pdf")