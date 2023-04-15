from fpdf import FPDF

client = ""
title = "SEO Audit {}".format(client)

pdf = FPDF()
pdf.set_title(title)
pdf.set_author('Jules Verne')


pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'SEO Audit Report')
pdf.cell(40, 30, 'Powered by FPDF.')

pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 30, 'Powered by FPDF.')
pdf.output('test.pdf', 'F')
