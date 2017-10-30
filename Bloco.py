import Registro

QTD_REGISTROS_BLOCO = 5     # o bloco será composto de até 5 registros
TAM_BLOCO = 512             #definindo tamanho do bloco
TAM_REGISTRO = 100          #definindo tamanho do registro

class Bloco (object):

    def __init__(self):
        self.qtdRegistros = "0"
        self.Registros = []
        self.complemento = "___________" # 11 "_" para completar o bloco que deve conter 512 bytes
        self.completaRegistroVazio()    # coloca os 5 registros vazios

    def verificaPossibilidadeInsercao(self):
        if int(self.qtdRegistros) < QTD_REGISTROS_BLOCO:
            return 1
        else:
            return 0

    def completaRegistroVazio(self):
        for i in range(0, QTD_REGISTROS_BLOCO):
            registro = Registro.Registro("","","","")
            self.Registros.append(registro)

    def retornaString(self):
        string = self.qtdRegistros
        for i in range(0,QTD_REGISTROS_BLOCO):
            string += self.Registros[i].retornaString()
        string += self.complemento
        return string

    def completaAtravesString(self, string):
        if(len(string) == TAM_BLOCO):           #apenas confirmando que está no tamanho certo
            self.qtdRegistros = string[0]
            final = 1
            for i in range(0,QTD_REGISTROS_BLOCO):
                inicio = final
                final += TAM_REGISTRO
                self.Registros[i].completaAtravesString(string[inicio:final])

    def incrementaQtdRegistros(self):
        qtd = int(self.qtdRegistros)
        qtd += 1
        self.qtdRegistros = str(qtd)

    def decrementaQtdRegistros(self):
        qtd = int(self.qtdRegistros)
        qtd -= 1
        self.qtdRegistros = str(qtd)

    def exibeBloco(self):
        print("Quantidade de registros: " + self.qtdRegistros)
        for i in range(0,QTD_REGISTROS_BLOCO):
            self.Registros[i].exibeRegistro()
            print("\n")

    def exibeRegistrosDoBloco(self):
        for i in range(0,int(self.qtdRegistros)):
            if self.Registros[i].RA[0]!= "#" and self.Registros[i].RA[0]!= "_":
                self.Registros[i].exibeRegistro()
                print("\n")

    def numeroRegistroInvalido(self):
        for i in range(0,int(self.qtdRegistros)):
            if self.Registros[i].RA[0]== "#":
                return int(i)
        return int(-1)

    def formatarTodosRegistros(self):
        for i in range(0, QTD_REGISTROS_BLOCO):
            registro = Registro.Registro("","","","")
            self.Registros[i] = registro

    def formatarBloco(self):
        self.qtdRegistros = "0"
        self.formatarTodosRegistros()    # coloca os 5 registros vazios
