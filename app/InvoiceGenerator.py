# Importing Required Module
from reportlab.pdfgen import canvas
import uuid
from datetime import date

class InvoiceGenerator:
    invoiceNumber = uuid.uuid4().hex
    parts = []
    partCoordinateY = 125

    c = canvas.Canvas("invoice" + str(invoiceNumber) + ".pdf", pagesize=(200, 250), bottomup=0)

    def createTemplate(self):
        # Creating Canvas

        # Logo Section
        # Setting th origin to (10,40)
        self.c.translate(10,40)
        # Inverting the scale for getting mirror Image of logo
        self.c.scale(1,-1)
        # Inserting Logo into the Canvas at required position
        self.c.drawImage("ej engine.jpg",0,0,width=50,height=30)
        # Title Section
        # Again Inverting Scale For strings insertion
        self.c.scale(1,-1)
        # Again Setting the origin back to (0,0) of top-left
        self.c.translate(-10,-40)
        # Setting the font for Name title of company
        self.c.setFont("Helvetica-Bold",10)
        # Inserting the name of the company
        self.c.drawCentredString(125,20,"Database Dads Auto Parts")
        # For under lining the title
        self.c.line(70,22,180,22)
        # Changing the font size for Specifying Address
        self.c.setFont("Helvetica-Bold",5)
        self.c.drawCentredString(125,30,"201 Meadow Brook Road")
        self.c.drawCentredString(125,35,"Rochester, MI 48309")
        # Changing the font size for Specifying GST Number of firm
        # Line Seprating the page header from the body
        self.c.line(5,45,195,45)
        # Document Information
        # Changing the font for Document title
        self.c.setFont("Courier-Bold",8)
        self.c.drawCentredString(100,55,"INVOICE")
        # This Block Consist of Costumer Details
        self.c.roundRect(15,63,170,40,10,stroke=1,fill=0)
        # This Block Consist of Item Description
        self.c.roundRect(15,108,170,130,10,stroke=1,fill=0)
        self.c.line(15,120,185,120)
        self.c.setFont("Courier-Bold", 5)
        self.c.drawCentredString(25,118,"Part #")
        self.c.drawCentredString(75,118,"PART DESCRIPTION")
        self.c.drawCentredString(125,118,"PRICE")
        self.c.drawCentredString(148,118,"QTY")
        self.c.drawCentredString(173,118,"TOTAL")
        # Drawing table for Item Description
        self.c.line(15,210,185,210)
        self.c.line(35,108,35,220)
        self.c.line(115,108,115,220)
        self.c.line(135,108,135,220)
        self.c.line(160,108,160,220)

        # Declaration and Signature
        self.c.line(15,220,185,220)
        self.c.line(100,220,100,238)
        self.c.setFont("Courier-Bold", 3)
        self.c.drawString(20,225,"(This is system generated invoice)")
        self.c.setFont("Courier-Bold", 5)
        self.c.drawCentredString(130,225,"Customer Signature:")

    def addInvoiceInfo(self, phone):
        self.c.setFont("Times-Bold", 5)
        self.c.drawCentredString(90, 70, "INVOICE No. : " + str(self.invoiceNumber))
        self.c.drawCentredString(90, 80, "DATE :" + str(date.today()))
        self.c.drawCentredString(90, 90, "CUSTOMER PHONE :" + str(phone))

    def addPartToInvoice(self, part):
        self.c.drawCentredString(25, self.partCoordinateY, str(part))
        self.c.drawCentredString(75, self.partCoordinateY, "Brake Pad")
        self.c.drawCentredString(125, self.partCoordinateY, str(19.99))
        self.c.drawCentredString(148, self.partCoordinateY, str(1))
        self.partCoordinateY += 5
        return

    def finishAndSaveInvoice(self):
        self.c.setFont("Times-Bold", 5)
        self.c.drawCentredString(173, 216, str(40.00))
        # End the Page and Start with new
        self.c.showPage()
        # Saving the PDF
        self.c.save()

Invoice = InvoiceGenerator()
Invoice.createTemplate()
Invoice.addInvoiceInfo("248-555-5555")
Invoice.addPartToInvoice(6969)
Invoice.addPartToInvoice(1234)
Invoice.finishAndSaveInvoice()