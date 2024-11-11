from fpdf import FPDF
titulo = '20.000 Léguas submarinas'

class PDF(FPDF):
    def header(self):
    
        self.set_font('helvetica', 'B',15)
        
        
        titulo_w = self.get_string_width(titulo) + 6
        doc_w = self.w
        self.set_x((doc_w - titulo_w) / 2)

        
        self.set_draw_color(0,80,180) #Borda = Azul
        self.set_fill_color(230,230,0) #Background = Amarelo
        self.set_text_color(220,50,50) # texto = Vermelho

        
        self.set_line_width(1)


        
        self.cell(titulo_w,10,titulo, border=True,align='C', fill=1 )
        self.ln(20)
    
    def footer(self):
        #Posicao do rodape
        self.set_y(-15)
        #Fonte
        self.set_font('helvetica', 'I', 8)
        #Cor da fonte Cinza
        self.set_text_color(169,169,169)
        #Numero da pagina
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')

    def titulo_do_capitulo(self,numeroCapitulo,tituloCapitulo,link):
        #Link  location
        self.set_link(link)

        #Fonte
        self.set_font('helvetica', '', 12)
        #Cor do fundo
        self.set_fill_color(200,220,255)
        #Titulo do capitulo
        titulo_do_capitulo = f'Capítulo {numeroCapitulo} : {tituloCapitulo}'
        self.cell(0,5,titulo_do_capitulo, fill=1)
        self.ln(10)

    def conteudo(self,name):
        #Lendo o arqquivo txt
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #Fonte
        self.set_font('times','',12)
        #inserindo texto
        self.multi_cell(0,5,txt)
        self.ln()
        #Final de cada capitulo
        self.set_font('times', 'I', 12)
        self.cell(0,5,'FIM DO CAPITULO')
    
    
    def printCapitulo(self,cap_num,cap_titulo, nome, link):
        self.add_page()
        self.titulo_do_capitulo(cap_num, cap_titulo, link)
        self.conteudo(nome)


pdf = PDF('P','mm','Letter') #Com a classe PDF criada, não á necessidade de colocar esta instancia de pdf = FPDF, pois a classe PDF já herda o FPDF

##Metadata
pdf.set_title(titulo)
pdf.set_author('Jules Verne')


# Quando houver o link do arquivo txt colocar na variavel website
website = "nda"
cap1_link = pdf.add_link()
cap2_link = pdf.add_link()



#Inserindo quebra de pagina automatica
pdf.set_auto_page_break(auto=True, margin=20)

pdf.add_page()
pdf.image('backGround20mil.png', x=-0.5,w=pdf.w +1)

#Link anexo
pdf.cell(0,10,'Fonte do texto', link=website)
pdf.ln()
#pdf.cell(0,10,'Capítulo 1 ', link=cap1_link)
#pdf.ln()
#pdf.cell(0,10,'Capítulo 2 ', link=cap2_link)


pdf.printCapitulo(1,'UM RECIFE ARISCO','cap1.txt',cap1_link)
pdf.printCapitulo(2, 'PRÓS E CONTRAS','cap2.txt', cap2_link)

pdf.output('pdf_4.pdf')