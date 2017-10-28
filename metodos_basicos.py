import Registro
from metodos_extras import tamanhoCorreto
import os.path

TAM_RA = 6          #definindo tamanho do campo RA
TAM_NOME = 44       #definindo tamanho do campo nome
TAM_CURSO = 30      #definindo tamanho do campo curso
TAM_CIDADE = 20     #definindo tamanho do campo cidade
TAM_REGISTRO = 100  #definindo tamanho total do registro

def criaArquivo():
    #criando arquivo vazio
    arq = open("arquivo.txt", 'w')
    arq.close()
    print("\nArquivo vazio criado com sucesso\n")


def insere():

    if(os.path.exists("arquivo.txt")):
        ra = input('\nDigite o RA: ')
        nome = input('Digite o nome: ')
        curso = input('Digite o curso: ')
        cidade = input('Digite a cidade: ')

        registro = Registro.Registro(ra, nome, curso, cidade)

        #abrindo arquivo (ou criando, se nao existir) e escrevendo a string registro nele
        arq = open("arquivo.txt", 'a') # 'a' pois anexa ao conteudo anterior
        arq.write(registro.retornaString())
        arq.close()
    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de inserir, selecione a opção para criar!\n")

def busca(chave):
    if(os.path.exists("arquivo.txt")): # verifica se o arquivo existe
        chave = tamanhoCorreto(chave,TAM_RA)     #transformando a chave recebida no mesmo formato do campo RA
        posicao = 0
        encontrou = 0
        arq = open("arquivo.txt", 'r') # 'r' pois deseja apenas leitura
        arq.seek(posicao)
        while(not encontrou):
            w = arq.read(TAM_RA) #le uma palavra correspondente ao tamanho do campo RA
            if w == "":     #se for vazio, significa que acabou o arquivo
                break
            elif w[0] != "#" and w == chave: # pois "#" indica que o registro foi removido
                encontrou = 1
            else:
                posicao += TAM_REGISTRO      #se nao encontrou, como o registro tem tamanho fixo de 100 bytes, vai pro proximo registro, isto é, dali 100 posicoes
                arq.seek(posicao)


        if encontrou:
            encontrou = 0
            arq.seek(posicao)
            registro = Registro.Registro("","","","")
            registro.RA = arq.read(TAM_RA)
            registro.nome = arq.read(TAM_NOME)
            registro.curso = arq.read(TAM_CURSO)
            registro.cidade = arq.read(TAM_CIDADE)
            return registro

        arq.close()
    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de buscar, selecione a opção para criar!\n")


    return None   # se não encontrou a chave ou se o arquivo nao existe


def remove(chave):
    if(os.path.exists("arquivo.txt")): # verifica se o arquivo existe
        chave = tamanhoCorreto(chave,TAM_RA)     #transformando a chave recebida no mesmo formato do campo RA
        posicao = 0
        encontrou = 0
        arq = open("arquivo.txt", 'r+') # 'r+' pois deseja é leitura e escrita
        while(not encontrou):
            w = arq.read(TAM_RA) #le uma palavra correspondente ao tamanho do campo RA
            if w == "":     #se for vazio, significa que acabou o arquivo
                break
            elif w[0] != "#" and w == chave: # pois "#" indica que o registro foi removido
                encontrou = 1
            else:
                posicao += TAM_REGISTRO      #se nao encontrou, como o registro tem tamanho fixo de 100 bytes, vai pro proximo registro, isto é, dali 100 posicoes
                arq.seek(posicao)


        if encontrou:
            arq.seek(posicao)
            arq.write("#")
            return 1

        arq.close()

    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de remover um registro, selecione a opção para criar!\n")


    return 0   # se não encontrou a chave ou se o arquivo nao existe
