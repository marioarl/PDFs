from fpdf import FPDF
titulo = '20.000 Léguas submarinas'

class PDF(FPDF):
    #cabecalho
    def header(self):
        #Fonte
        self.set_font('helvetica', 'B',15)
        
        #Calcular largura do Titulo e posição
        titulo_w = self.get_string_width(titulo) + 6
        doc_w = self.w
        self.set_x((doc_w - titulo_w) / 2)

        #Cores do Frame,Background e text
        self.set_draw_color(0,80,180) #Borda = Azul
        self.set_fill_color(230,230,0) #Background = Amarelo
        self.set_text_color(220,50,50) # texto = Vermelho

        #Largura do  Frame(Borda)
        self.set_line_width(1)


        #Titulo
        self.cell(titulo_w,10,titulo, border=True,align='C', fill=1 )
        self.ln(20)
    
    #Rodapé
    def footer(self):
        #Posicao do rodape
        self.set_y(-15)
        #Fonte
        self.set_font('helvetica', 'I', 8)
        #Cor da fonte Cinza
        self.set_text_color(169,169,169)
        #Numero da pagina
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')

    #Adicionando titulo em cada capitulo
    def titulo_do_capitulo(self,numeroCapitulo,tituloCapitulo):
        #Fonte
        self.set_font('helvetica', '', 12)
        #Cor do fundo
        self.set_fill_color(200,220,255)
        #Titulo do capitulo
        titulo_do_capitulo = f'Capítulo {numeroCapitulo} : {tituloCapitulo}'
        self.cell(0,5,titulo_do_capitulo, fill=1)
        self.ln(10)

    #Conteudo dos capitulos
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
    
    #Imprimindo os capitulos
    def printCapitulo(self,cap_num,cap_titulo, nome):
        self.add_page()
        self.titulo_do_capitulo(cap_num, cap_titulo)
        self.conteudo(nome)


pdf = PDF('P','mm','Letter') #Com a classe PDF criada, não á necessidade de colocar esta instancia de pdf = FPDF, pois a classe PDF já herda o FPDF

#Total de numero de paginas
pdf.alias_nb_pages()

#Inserindo quebra de pagina automatica
pdf.set_auto_page_break(auto=True, margin=20)

pdf.add_page()

pdf.printCapitulo(1,'UM RECIFE ARISCO','cap1.txt')
pdf.printCapitulo(2, 'PRÓS E CONTRAS','cap2.txt')

pdf.output('pdf_3.pdf')