import Registro
                            # Como 1 byte = 1 caracter
QTD_REGISTROS_BLOCO = 5     # o bloco sera composto de ate 5 registros
TAM_BLOCO = 512             # definindo tamanho do bloco (512 bytes)
TAM_REGISTRO = 100          # definindo tamanho do registro (100 bytes)

class Bloco (object):

    # Metodo construtor
    def __init__(self):
        self.qtdRegistros = "0"          # variavel que indica quantidade de registros no bloco, iniciada com 0
        self.Registros = []              # vetor de registros, inicializa vazio
        self.complemento = "___________" # 11 "_" para completar o bloco que deve conter 512 bytes
        self.completaRegistroVazio()     # método para colocar os 5 registros vazios no vetor Registros


    # Metodo para verificar se ainda existem registros nao ocupados no bloco
    # Nao possui parametros
    # Retorno:  1 para indicar que pode inserir registro ao final
    #           0 para indicar que nao pode inserir registro ao final
    def verificaPossibilidadeInsercao(self):
        if int(self.qtdRegistros) < QTD_REGISTROS_BLOCO:        # verifica se ha espaço suficiente para inserir novo registro no bloco
            return 1
        else:
            return 0


    # Metodo que inicializa o vetor Registros com 5 registros vazios
    # Nao possui parametros
    # Nao possui retorno
    def completaRegistroVazio(self):
        for i in range(0, QTD_REGISTROS_BLOCO):
            registro = Registro.Registro("","","","")
            self.Registros.append(registro)             # preenchendo registros vazios


    # Metodo que retorna todo o conteudo do bloco no formato de uma string
    # Nao possui parametros
    # Retorno: string com todo conteudo do bloco concatenado na sequencia (qtdRegistros, conteudo de cada Registro[i], complemento)
    def retornaString(self):
        string = self.qtdRegistros
        for i in range(0,QTD_REGISTROS_BLOCO):
            string += self.Registros[i].retornaString()
        string += self.complemento
        return string


    # Metodo que recebe uma string e completa o conteudo do bloco com ela
    # Parametro: string com conteudo a ser preenchido no bloco
    # Nao possui retorno
    def completaAtravesString(self, string):
        if(len(string) == TAM_BLOCO):           # apenas confirmando que esta no tamanho certo (512)
            self.qtdRegistros = string[0]
            final = 1
            for i in range(0,QTD_REGISTROS_BLOCO):
                inicio = final
                final += TAM_REGISTRO
                self.Registros[i].completaAtravesString(string[inicio:final])


    # Metodo que incrementa em 1 a variavel que indica a quantidade de registros no bloco
    # Nao possui parametros
    # Nao possui retorno
    def incrementaQtdRegistros(self):
        qtd = int(self.qtdRegistros)
        qtd += 1
        self.qtdRegistros = str(qtd)


    # Metodo que decrementa em 1 a variavel que indica a quantidade de registros no bloco
    # Nao possui parametros
    # Nao possui retorno
    def decrementaQtdRegistros(self):
        qtd = int(self.qtdRegistros)
        qtd -= 1
        self.qtdRegistros = str(qtd)


    # Metodo que exibe na tela todas as informacoes do bloco
    # Nao possui parametros
    # Nao possui retorno
    def exibeBloco(self):
        print("Quantidade de registros: " + self.qtdRegistros)
        for i in range(0,QTD_REGISTROS_BLOCO):
            self.Registros[i].exibeRegistro()        # exibe conteúdo de cada registro
            print("\n")


    # Metodo exibe na tela apenas os registros validos do bloco
    # Nao possui parametros
    # Nao possui retorno
    def exibeRegistrosDoBloco(self):
        for i in range(0,int(self.qtdRegistros)):
            if self.Registros[i].RA[0]!= "#" and self.Registros[i].RA[0]!= "_":
                self.Registros[i].exibeRegistro()
                print("\n")


    # Metodo que encontra o indice do primeiro registro invalido que encontrar
    # Nao possui parametros
    # Retorno: se houver, retorna indice do primeiro registro invalido encontrado
    #          se nao houver, retorna -1
    def numeroRegistroInvalido(self):
        for i in range(0,QTD_REGISTROS_BLOCO):
            if self.Registros[i].RA[0]== "#":
                return int(i)
        return int(-1)


    # Metodo que formata o conteudo de todos os registros, isto é, retorna ao vazio
    # Nao possui parametros
    # Nao possui retorno
    def formatarTodosRegistros(self):
        for i in range(0, QTD_REGISTROS_BLOCO):
            registro = Registro.Registro("","","","")
            self.Registros[i] = registro            # coloca todos os registros como vazio


    # Metodo que formata todo o conteudo do bloco, isto é, retorna ao estado inicial vazio
    # Nao possui parametros
    # Nao possui retorno
    def formatarBloco(self):
        self.qtdRegistros = "0"
        self.formatarTodosRegistros()    # coloca os 5 registros vazios
