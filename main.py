from fpdf import FPDF

# Generate PDF
pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape
pdf.set_auto_page_break(auto=False, margin=0) # pages should not be broken automatically

# Create a blank page
pdf.add_page()

# Lines and spacing
pdf.line(20, 28, 190, 28)
pdf.line(20, 32, 190, 32)
pdf.line(20, 36, 190, 36)
pdf.line(20, 40, 190, 40)
pdf.line(20, 44, 190, 44)
pdf.line(20, 48, 190, 48)

# Give output
pdf.output("output/empty-tab-sheet.pdf")