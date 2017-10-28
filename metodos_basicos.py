import Registro
import Bloco
from metodos_extras import tamanhoCorreto
import os.path

TAM_RA = 6                  #definindo tamanho do campo RA
TAM_NOME = 44               #definindo tamanho do campo nome
TAM_CURSO = 30              #definindo tamanho do campo curso
TAM_CIDADE = 20             #definindo tamanho do campo cidade
TAM_REGISTRO = 100          #definindo tamanho total do registro
TAM_BLOCO = 512             #definindo tamanho total do bloco
TAM_CABECALHO_BLOCO = 1     #definindo tamanho do cabeçalho do bloco
TAM_COMPLEMENTO_BLOCO = 11  #definindo tamanho do complemento do bloco

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

        novo_registro = Registro.Registro(ra, nome, curso, cidade)

        bloco = Bloco.Bloco()

        posicao = 0
        fim = 0

        #abrindo arquivo e encontrando o bloco a ser inserido
        arq = open("arquivo.txt", 'r+') # 'r+' pois primeiro será feito leitura para encontrar o bloco e depois será inserido
        #arq.write(registro.retornaString())

        arq.seek(posicao)
        while(not fim):
            w = arq.read(TAM_CABECALHO_BLOCO) #le o cabeçalho do bloco
            if w == "":
                fim = 1
                # insere novo bloco
                bloco.Registros[0] = novo_registro
                bloco.incrementaQtdRegistros()
                arq.write(bloco.retornaString())

            elif int(w) < 5:     #se ainda couber registro no bloco
                fim = 1
                # insere registro no bloco
                arq.seek(posicao)
                string = arq.read(TAM_BLOCO)
                arq.seek(posicao)

                bloco.completaAtravesString(string)

                bloco.Registros[int(w)] = novo_registro

                bloco.incrementaQtdRegistros()

                arq.write(bloco.retornaString())

            else:
                posicao += TAM_BLOCO      #se nao cabe mais nesse bloco, como ele tem tamanho fixo de 512 bytes, vai pro proximo bloco, isto é, dali 512 posicoes
                arq.seek(posicao)

        print("\nNovo registro inserido com sucesso!")
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
            w = arq.read(TAM_CABECALHO_BLOCO) #le uma palavra correspondente ao cabecalho do bloco
            if w == "":     #se for vazio, significa que acabou o arquivo
                break
            elif int(w) > 0:
                posicao += 1
                for i in range(0,int(w)):   #percorre todos os registros daquele bloco
                    ra = arq.read(TAM_RA)   #le uma palavra correspondente ao tamanho do campo RA
                    if ra[0] != "#" and ra == chave: # pois "#" indica que o registro foi removido
                        encontrou = 1
                        break
                    else:
                        posicao += TAM_REGISTRO      #se nao encontrou, como o registro tem tamanho fixo de 100 bytes, vai pro proximo registro, isto é, dali 100 posicoes
                        arq.seek(posicao)
                if (not encontrou) and int(w) == 5:
                    posicao += TAM_COMPLEMENTO_BLOCO
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
            w = arq.read(TAM_CABECALHO_BLOCO) #le uma palavra correspondente ao cabecalho do bloco
            if w == "":     #se for vazio, significa que acabou o arquivo
                break
            elif int(w) > 0:
                posicao += 1
                for i in range(0,int(w)):   #percorre todos os registros daquele bloco
                    ra = arq.read(TAM_RA)   #le uma palavra correspondente ao tamanho do campo RA
                    if ra[0] != "#" and ra == chave: # pois "#" indica que o registro foi removido
                        encontrou = 1
                        break
                    else:
                        posicao += TAM_REGISTRO      #se nao encontrou, como o registro tem tamanho fixo de 100 bytes, vai pro proximo registro, isto é, dali 100 posicoes
                        arq.seek(posicao)
                if (not encontrou) and int(w) == 5:
                    posicao += TAM_COMPLEMENTO_BLOCO
                    arq.seek(posicao)

        if encontrou:
            arq.seek(posicao)
            arq.write("#")
            return 1

        arq.close()

    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de remover um registro, selecione a opção para criar!\n")


    return 0   # se não encontrou a chave ou se o arquivo nao existe
