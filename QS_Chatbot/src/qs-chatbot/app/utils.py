from fpdf import FPDF

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Adicionando o texto ao PDF
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))
    
    # Salvando o PDF em um buffer
    pdf_output = pdf.output(dest='S').encode('latin-1')
    return pdf_output
