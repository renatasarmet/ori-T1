from metodos_extras import tamanhoCorreto

                    # Como 1 byte = 1 caracter
TAM_RA = 6          # definindo tamanho do campo RA (6 bytes)
TAM_NOME = 44       # definindo tamanho do campo nome (44 bytes)
TAM_CURSO = 30      # definindo tamanho do campo curso (30 bytes)
TAM_CIDADE = 20     # definindo tamanho do campo cidade (20 bytes)
TAM_REGISTRO = 100  # definindo tamanho total do registro (100 bytes)

# Utilizaremos registros de tamanho fixo com campos de tamanho fixo
class Registro (object):

    # Metodo construtor
    def __init__(self, RA, nome, curso, cidade):

        # garantindo que todos os dados sejam armazenados com exatamente o tamanho determinado, nem menos, nem mais
        # RA deve conter 6 bytes
        # nome deve conter 44 bytes
        # curso deve conter 30 bytes
        # cidade deve conter 20 bytes
        # Totalizando registro com tamanho de 100 bytes

        self.RA = tamanhoCorreto(RA,TAM_RA)
        self.nome = tamanhoCorreto(nome,TAM_NOME)
        self.curso = tamanhoCorreto(curso,TAM_CURSO)
        self.cidade = tamanhoCorreto(cidade,TAM_CIDADE)



    # Metodo que retorna o conteudo do registro em uma string
    # Nao possui parametros
    # Retorno:  string contendo o conteudo do registro, concatenado na sequencia (RA + nome + curso + cidade)
    def retornaString(self):
        return self.RA + self.nome + self.curso + self.cidade       # retorna todo o registro como uma unica string


    # Metodo que exibe na tela todo o conteudo do registro
    # Nao possui parametros
    # Nao possui retorno
    def exibeRegistro(self):
        RA = self.RA.replace("_","")        # substitui '_' por '' para nao exibir a parte que sobrou no campo
        nome = self.nome.replace("_","")
        curso = self.curso.replace("_","")
        cidade = self.cidade.replace("_","")

        print("RA: " + RA)
        print("Nome: " + nome)
        print("Curso: " + curso)
        print("Cidade: " + cidade)


    # Metodo que recebe uma string e completa o conteudo do registro a partir dela
    # Parametro: string que contem o conteudo a ser preenchido no registro
    # Nao possui retorno
    def completaAtravesString(self, string):
        if(len(string) == TAM_REGISTRO):        # garante que a string seja do tamanho certo, entao preenche os campos
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


    # Metodo que formata o registro, colocando todos os campos como vazios
    # Nao possui parametros
    # Nao possui retorno
    def formatarRegistro(self):             # coloca o registro como vazio
        self.RA = tamanhoCorreto("", TAM_RA)
        self.nome = tamanhoCorreto("",TAM_NOME)
        self.curso = tamanhoCorreto("",TAM_CURSO)
        self.cidade = tamanhoCorreto("",TAM_CIDADE)

    # Metodo que realiza a remocao logica do registro
    # Nao possui parametro
    # Nao possui retorno
    def removeLogicamente(self):            # remocao logica, com marcação sinalizada por '#'
        self.RA = tamanhoCorreto("#", TAM_RA)       # como o RA é a chave e o primeiro elemento, ele sera utilizado para marcacao na remocao logica
