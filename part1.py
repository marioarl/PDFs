from fpdf import FPDF

#Criando um objeto FPDF
'''
utiliza-se o FPDF com os seguintes argumentos:
Layout ('P','L') ==> Portrait, Landscape
Unidade('mm', 'cm', 'in') ==> Milimetros,Centimetros e Polegadas
Formato('A3','A4 (default)', 'A5', 'Letter', 'Legal', (100,50)custom)
'''
pdf = FPDF('P','mm','Letter')

#Adicionando Página
pdf.add_page()

#Fontes
'''
Fontes('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
Modo('B' (bold) 'U' (underline), 'I' (italico) '' (regular), combination (i.e. ('BU'))
Tamanho(ex 16)
'''
pdf.set_font('helvetica','',16)

#Adicionando Text
pdf.set_fill_color(200,220,255) #Configura a cor de fundo da celula
'''
w = largura da celula, se w=0 a celula se estenderá ate a magem direita
h = altura
txt = Seu texto
border (0 False, 1 True - Insere uma borda em torno da celula , L(esquerda),T(Topo),R(direita),B(baixo))
align = alinhamento
fill = preenchimento de fundo (Se True preenche a celula com a cor de fundo configurada)
link = Link para URL
'''
pdf.cell(120, 100,'Hello World!', border=1,align='C', fill=True)

pdf.ln(80) #Insere uma linha abaixo (parametro de quantidade de acordo com a especificada ex. mm)
pdf.cell(80, 100, 'Good Bye Wold!')


pdf.output('pdf_1.pdf')