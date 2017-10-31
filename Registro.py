from metodos_extras import tamanhoCorreto

TAM_RA = 6          # definindo tamanho do campo RA
TAM_NOME = 44       # definindo tamanho do campo nome
TAM_CURSO = 30      # definindo tamanho do campo curso
TAM_CIDADE = 20     # definindo tamanho do campo cidade
TAM_REGISTRO = 100  # definindo tamanho total do registro

class Registro (object):

    def __init__(self, RA, nome, curso, cidade):

        # garantindo que todos os dados sejam armazenados com exatamente o tamanho determinado, bem menos, nem mais
        # RA deve conter 6 bytes
        # nome deve conter 44 bytes
        # curso deve conter 30 bytes
        # cidade deve conter 20 bytes

        self.RA = tamanhoCorreto(RA,TAM_RA)
        self.nome = tamanhoCorreto(nome,TAM_NOME)
        self.curso = tamanhoCorreto(curso,TAM_CURSO)
        self.cidade = tamanhoCorreto(cidade,TAM_CIDADE)


    def retornaString(self):
        return self.RA + self.nome + self.curso + self.cidade       # retorna todo o registro como uma única string

    def exibeRegistro(self):        
        RA = self.RA.replace("_","")        # substitui '_' por ''
        nome = self.nome.replace("_","")
        curso = self.curso.replace("_","")
        cidade = self.cidade.replace("_","")

        print("RA: " + RA)
        print("Nome: " + nome)
        print("Curso: " + curso)
        print("Cidade: " + cidade)

    def completaAtravesString(self, string):
        if(len(string) == TAM_REGISTRO):        # se a string tiver o mesmo numero de bytes que o tamanho do registro (100 bytes), preenche os campos
            inicio = 0
            final = TAM_RA
            self.RA = string[inicio:final]
            inicio = final
            final += TAM_NOME
            self.nome = string[inicio:final]
            inicio = final
            final += TAM_CURSO
            self.curso = string[inicio:final]
            inicio = final
            final += TAM_CIDADE
            self.cidade = string[inicio:final]

    def formatarRegistro(self):             # coloca o registro como vazio
        self.RA = tamanhoCorreto("", TAM_RA)
        self.nome = tamanhoCorreto("",TAM_NOME)
        self.curso = tamanhoCorreto("",TAM_CURSO)
        self.cidade = tamanhoCorreto("",TAM_CIDADE)

    def removeLogicamente(self):            # remocao logica, com marcação sinalizada por '#'
        self.RA = tamanhoCorreto("#", TAM_RA)       # como o RA é a chave, ele sera utilizado para marcacao na remocao logica
