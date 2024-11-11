#Criando um PDF com um titulo, Logo ou imagem, quebra de pagina automaticas, rodapes com numero de paginas
'''
Colocar a imagem que voce precisa na pasta do programa
'''
from fpdf import FPDF

#Adicinando cabecalho e rodapé
'''
Para adicionar cabecalho e rodapé, precisamos estender a classe e substitui-los

'''
class PDF(FPDF):
    #cabecalho
    def header(self):
        #logo
        '''
        nome(str): O caminho ou URL da imagem a ser inserida
            *Este parametro é obrigatorio e especifica o arquivo de imagem a ser inserido no PDF. Pode ser uma imagem local ou um link para uma imagem na Web
        x (float, opcional): A posicao horizontal (em mm) onde a imagem será inserida
            *Se nao for especificado a imagem sera colocada na posicao atual do cursor
        y (float, opcional): A posicao vertical (em mm) onde a imagem será inserida
            *Se nao for especificado a imagem sera colocada na posicao atual do cursor
        w (float, opcional): Largura da imagem(em mm)
            *Se w for definido como 0, a largura sera ajustada automaticamente para manter a proporcao original da imagem
            *Se w for especificado e h for 0, a altura será ajustada proporcionalmente a largura fornecida
        h(float, opcional): Altura da imagem (em mm)
            *Se h for definido como 0, a altura sera ajustada automaticamente para manter a proporcao original da imagem
            *Se h for especificado e w for 0, a altura será ajustada proporcionalmente a altura fornecida
        type (str,opcional): Tipo de imagem
            *Geralmente o type é detectado automaticamente com base na extensao do arquivo da imagem(ex .jpg, .png), mas se necessario, voce pode especifica-lo (ex: 'JPEG', 'PNG')
        link (str ou URL, opcional): define um link que sera associado a imagem
            *Quando o usuario clicar na imagem, ele será direcionado para URL ou link especificado
        '''
        self.image('abacaxi.png', 10,8,25)
        #Fonte do cabecalho
        self.set_font('helvetica', 'B',20)
        #Padding
        self.cell(80)
        #Titulo
        self.cell(30,10,'Titulo', border=True,align='C' )
        self.ln(20)
    
    #Rodapé
    def footer(self):
        #Posicao do rodape
        self.set_y(-15)
        #Fonte
        self.set_font('helvetica', 'I', 10)
        #Numero da pagina
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')

pdf = PDF('P','mm','Letter') #Com a classe PDF criada, não á necessidade de colocar esta instancia de pdf = FPDF, pois a classe PDF já herda o FPDF

#Total de numero de paginas
pdf.alias_nb_pages()

#Inserindo quebra de pagina automatica
'''
auto(bool):Ativa ou desativa a quebra automatica de página
    *True: Ativa a quebra automática de página
    *False: Desativa a quebra automatica de pagina.Com isso voce precisará gerenciar manualmente quando adicionar uma nova pagina
margin(float): Define a margem inferior da página, onde a quebra ocorrerá(padrao 0)
    *Este parametro define a distancia entre a parte inferior da pagina e o conteudo. Quando o conteudo se aproxima dessa margem, uma nova pagina será criada automaticamante
'''
pdf.set_auto_page_break(auto=True, margin=20)

pdf.add_page()
pdf.set_font('times','',12)

#Inserindo linhas no PDF
for i in range(1,41):
    pdf.cell(0,10,f'Esta é a linha {i}')
    pdf.ln(10)

pdf.output('pdf_2.pdf')