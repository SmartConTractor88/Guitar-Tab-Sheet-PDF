from fpdf import FPDF

# Generate PDF
pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape
pdf.set_auto_page_break(auto=False, margin=0) # pages should not be broken automatically

# Create a blank page
pdf.add_page()

# Lines and spacing

lines_per_row = 6
line_spacing = 3.5 # pixels between lines
rows_per_sheet = 8
row_spacing = 8
from_top = 38

pdf.line(40, 20, 170, 20)

for row in range(rows_per_sheet):
    for line in range(lines_per_row):
        pdf.line(20, from_top, 190, from_top)
        from_top += line_spacing

    from_top += row_spacing # create space between rows


# Give output
pdf.output("output/empty-tab-sheet.pdf")