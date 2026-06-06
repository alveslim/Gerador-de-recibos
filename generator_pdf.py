from fpdf import FPDF
from num2words import num2words
from datetime import date

# layout do recibo

cliente = input("Digite o nome do cliente: ")
consulta = input("Digite a consulta realizada: ")
valor = input("Digite o valor do recibo: ")
vlr_msg = f"{valor} reais"
vlr_extenso = num2words(float(valor), lang='pt_BR')
vlr_extenso_msg = f"{vlr_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", size=20)
pdf.image("static/rec.jpg", x=0, y=0, w=210, h=297)
pdf.text(162, 45, vlr_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, vlr_extenso_msg)
pdf.text(80, 135, consulta)
pdf.set_text_color(255, 255, 255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))

nome = f"{cliente}_{consulta}_{ano}_{mes}_{dia}.pdf"

#pdf.cell(200, 10, txt="Hello World!", ln=1, align='C')
pdf.output(nome)
print(f"Recibo gerado com sucesso! Nome do arquivo: {nome}")