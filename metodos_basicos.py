import Registro
import Bloco
from metodos_extras import tamanhoCorreto
import os.path

TAM_RA = 6                  # definindo tamanho do campo RA (6 bytes)
TAM_NOME = 44               # definindo tamanho do campo nome (44 bytes)
TAM_CURSO = 30              # definindo tamanho do campo curso (30 bytes)
TAM_CIDADE = 20             # definindo tamanho do campo cidade (20 bytes)
TAM_REGISTRO = 100          # definindo tamanho total do registro (100 bytes)
TAM_BLOCO = 512             # definindo tamanho total do bloco (512 bytes)
TAM_CABECALHO_BLOCO = 1     # definindo tamanho do cabeçalho do bloco (1 byte)
TAM_COMPLEMENTO_BLOCO = 11  # definindo tamanho do complemento do bloco (11 bytes)

def criaArquivo():
    # criando arquivo vazio
    arq = open("arquivo.txt", 'w')
    arq.close()
    print("\nArquivo vazio criado com sucesso\n")


def insere():

    if(os.path.exists("arquivo.txt")):
        ra = input('\nDigite o RA (até 6 dígitos): ')
        nome = input('Digite o nome (até 44 dígitos): ')
        curso = input('Digite o curso (até 30 dígitos): ')
        cidade = input('Digite a cidade (até 20 dígitos): ')

        novo_registro = Registro.Registro(ra, nome, curso, cidade)      # insere os dados fornecidos no novo registro

        bloco = Bloco.Bloco()

        posicao = 0
        fim = 0

        # abrindo arquivo e encontrando o bloco a ser inserido
        arq = open("arquivo.txt", 'r+') # 'r+' pois primeiro será feito leitura para encontrar o bloco e depois será inserido

        while(not fim):
            arq.seek(posicao)
            string = arq.read(TAM_BLOCO)        # le conteudo do tamanho do bloco
            arq.seek(posicao)

            bloco.completaAtravesString(string)

            if string == "":
                bloco.formatarBloco()
                fim = 1
                # insere novo bloco
                bloco.Registros[0] = novo_registro      # insere registro no novo bloco 
                bloco.incrementaQtdRegistros()

            elif int(bloco.qtdRegistros) == 5:      # quantidade maxima de registros possiveis num bloco

                regInvalido = bloco.numeroRegistroInvalido() #verificando se o bloco possui algum registro invalido

                if regInvalido != -1:           # se existir registro invalido, substitui la
                    fim = 1
                    bloco.Registros[regInvalido] = novo_registro


            elif int(bloco.qtdRegistros) < 5:     #se ainda couber registro no bloco
                fim = 1
                # insere registro no bloco

                regInvalido = bloco.numeroRegistroInvalido() #verificando se o bloco possui algum registro invalido

                if regInvalido != -1:           # se existir registro invalido, substitui la
                    bloco.Registros[regInvalido] = novo_registro

                else:                           # se nao existir registro invalido, coloca no final
                    bloco.Registros[int(bloco.qtdRegistros)] = novo_registro
                    bloco.incrementaQtdRegistros()


            if (not fim):
                posicao += TAM_BLOCO      # se nao cabe mais nesse bloco, como ele tem tamanho fixo de 512 bytes, vai pro proximo bloco, isto é, dali 512 posicoes


        arq.write(bloco.retornaString())        # escreve registro no bloco
        print("\nNovo registro inserido com sucesso!")
        arq.close()
    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de inserir, selecione a opção para criar!\n")

def busca(chave):
    if(os.path.exists("arquivo.txt")): # verifica se o arquivo existe
        chave = tamanhoCorreto(chave,TAM_RA)     # transformando a chave recebida no mesmo formato do campo RA
        posicao = 0
        encontrou = 0
        bloco = Bloco.Bloco()
        arq = open("arquivo.txt", 'r') # 'r' pois deseja apenas leitura
        while(not encontrou):

            arq.seek(posicao)
            w = arq.read(TAM_BLOCO)     # le conteudo do tamanho do bloco, isto eh, 512 bytes
            arq.seek(posicao)
            bloco.completaAtravesString(w)

            if w == "":     # significa que acabou o arquivo
                break
            elif int(bloco.qtdRegistros) > 0:
                for i in range(0,int(bloco.qtdRegistros)):   # percorre todos os registros daquele bloco
                    if bloco.Registros[i].RA[0] != "#" and bloco.Registros[i].RA == chave: # pois "#" indica que o registro foi removido
                        regBuscado = i         # salva qual registro será removido
                        encontrou = 1
                        break

                if int(bloco.qtdRegistros) < 5:       # se tem menos que 5, entao é o ultimo bloco. Se nao encontrou aqui, nao está no arquivo
                    break

            posicao += TAM_BLOCO     # se nao encontrou nesse bloco vai para o próximo

        if encontrou:
            encontrou = 0
            registro = Registro.Registro("","","","")
            registro = bloco.Registros[regBuscado]
            return registro         # retorna o registro procurado

        arq.close()
    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de buscar, selecione a opção para criar!\n")


    return None   # se não encontrou a chave ou se o arquivo nao existe


def remove(chave):
    if(os.path.exists("arquivo.txt")):          # verifica se o arquivo existe
        chave = tamanhoCorreto(chave,TAM_RA)        # transformando a chave recebida no mesmo formato do campo RA
        posicao = 0
        encontrou = 0
        bloco = Bloco.Bloco()
        arq = open("arquivo.txt", 'r+') # 'r+' pois deseja leitura e escrita

        while(not encontrou):
            arq.seek(posicao)
            w = arq.read(TAM_BLOCO)
            arq.seek(posicao)
            bloco.completaAtravesString(w)

            if w == "" or w[0] == "0":     # significa que acabou o arquivo
                break
            elif int(bloco.qtdRegistros) > 0:
                for i in range(0,int(bloco.qtdRegistros)):      # percorre todos os registros daquele bloco
                    if bloco.Registros[i].RA[0] != "#" and bloco.Registros[i].RA == chave: # pois "#" indica que o registro foi removido
                        regRemovido = i         # salva qual registro será removido
                        encontrou = 1
                        break


                if int(bloco.qtdRegistros) < 5:       # se tem menos que 5 entao é o ultimo bloco. Se nao encontrou aqui, nao está no arquivo
                    break

            if (not encontrou):
                posicao += TAM_BLOCO     # se nao encontrou nesse bloco vai para o próximo


        if encontrou:
            bloco.Registros[regRemovido].removeLogicamente()        # marca o registro como removido
            arq.seek(posicao)
            arq.write(bloco.retornaString())
            return 1

        arq.close()

    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de remover um registro, selecione a opção para criar!\n")


    return 0   # se não encontrou a chave ou se o arquivo nao existe

def listagem():
    if(os.path.exists("arquivo.txt")):          # verifica se o arquivo existe
        bloco = Bloco.Bloco()
        posicao = 0
        fim = 0
        arq = open("arquivo.txt", 'r')          # 'r' pois deseja apenas leitura
        while(not fim):
            arq.seek(posicao)
            string = arq.read(TAM_BLOCO)
            bloco.completaAtravesString(string)

            if string == "":                    # se for vazio, significa que acabou o arquivo
                fim = 1
            elif int(bloco.qtdRegistros) > 0:       # se o bloco nao estiver vazio, exibe os registros
                bloco.exibeRegistrosDoBloco()
                posicao += TAM_BLOCO
            else:
                fim = 1

        arq.close()
    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de listar, selecione a opção para criar!\n")


    return None   # se não encontrou a chave ou se o arquivo nao existe



def compactacao():
    if(os.path.exists("arquivo.txt")):          # verifica se o arquivo existe
        posicaoIda = 0
        encontrou = 0
        fim = 0
        arq = open("arquivo.txt", 'r+')         # 'r+' pois deseja leitura e escrita
        posicaoVolta = os.path.getsize("arquivo.txt")           # inicia contagem no fim do arquivo
        posicaoApagar = posicaoVolta
        qtdBlocos = posicaoVolta / TAM_BLOCO    # armazena quantidade de blocos ainda nao percorridos pelo loop da volta
        posicaoVolta -= TAM_BLOCO               # coloca contagem no inicio do ultimo bloco
        while(not fim):
            blocoIda = Bloco.Bloco()
            while(not encontrou):
                arq.seek(posicaoIda)
                w = arq.read(TAM_BLOCO)         # le conteudo do tamanho do bloco, isto eh, 512 bytes
                arq.seek(posicaoIda)
                blocoIda.completaAtravesString(w)

                if w == "" or w[0] == "_":     #significa que acabou o arquivo
                    fim = 1
                    break
                elif int(blocoIda.qtdRegistros) > 0:
                    regInvalido = blocoIda.numeroRegistroInvalido()     # verificando se o bloco possui algum registro invalido

                    if regInvalido != -1:           # se existir registro invalido, encontrou
                        encontrou = 1
                        break

                posicaoIda += TAM_BLOCO     # se nao encontrou nesse bloco vai para o próximo

            if encontrou:                   # se encontrou, eh preciso realizar a remocao 
                encontrou = 0
                achouUltimo = 0
                blocoVolta = Bloco.Bloco()
                while(not achouUltimo):
                    if qtdBlocos > 0:
                        arq.seek(posicaoVolta)
                        w = arq.read(TAM_BLOCO)
                        arq.seek(posicaoVolta)

                        if posicaoVolta != posicaoIda:
                            blocoVolta.completaAtravesString(w)
                        else:
                            blocoVolta = blocoIda

                        if w == "" or w[0] == "0":        # bloco vazio, deveria ser apagado
                            #apagar esse bloco
                            posicaoApagar = posicaoVolta
                            pass

                        elif int(blocoVolta.qtdRegistros) > 0:
                            for i in range(int(blocoVolta.qtdRegistros)-1,-1,-1):             # percorre todos os registros daquele bloco em ordem descrescente
                                if blocoVolta.Registros[i].RA[0] != "#" and blocoVolta.Registros[i].RA[0] != "_":       # pois "#" indica que o registro teve remoção lógica e "_" ja nao tem registro
                                    if posicaoVolta > posicaoIda or (posicaoVolta == posicaoIda and i > regInvalido):      # confere se nao está fazendo troca repetida ou pelo mesmo registro
                                        regTrocaPosicao = i         # salva a posicao do ultimo registro que fará a troca com o inválido
                                        achouUltimo = 1
                                    break

                        if (not achouUltimo):
                            qtdBlocos -= 1          # mais um bloco percorrido, entao menos um bloco restante
                            posicaoVolta -= TAM_BLOCO           # coloca a contagem no inicio do bloco anterior
                            if posicaoVolta >= posicaoIda:
                                arq.seek(posicaoVolta)
                            else:
                                break
                    else:           # todos os blocos ja foram percorridos
                        break

                if achouUltimo:
                    w = blocoVolta.Registros[regTrocaPosicao].retornaString()   # pega o ultimo registro a ser copiado
                    blocoVolta.Registros[regTrocaPosicao].formatarRegistro()    # limpa ele
                    blocoVolta.decrementaQtdRegistros()                         # diminui a quantidade de registros no bloco
                    if blocoVolta.qtdRegistros == "0":
                        posicaoApagar = posicaoVolta
                    blocoIda.Registros[regInvalido].completaAtravesString(w)    # sobreescreve esse valor onde era o dado invalido
                    arq.seek(posicaoVolta)                                      # posiciona para escrever no arquivo o bloco da volta
                    arq.write(blocoVolta.retornaString())                       # escreve o bloco da volta no arquivo
                    arq.seek(posicaoIda)                                        #posiciona para escrever no arquivo o bloco da ida
                    arq.write(blocoIda.retornaString())                         # escreve o bloco da ida no arquivo

                else:
                    blocoIda.decrementaQtdRegistros()                           # diminui a quantidade de registros no bloco
                    if blocoIda.qtdRegistros == "0":
                        if posicaoIda < posicaoApagar:
                            posicaoApagar = posicaoIda
                    blocoIda.Registros[regInvalido].formatarRegistro()          # simplesmente formata o registro invalido
                    arq.seek(posicaoIda)                                        # posiciona para escrever no arquivo o bloco da ida
                    arq.write(blocoIda.retornaString())                         # escreve o bloco da ida no arquivo


                del(blocoVolta)
            del(blocoIda)


        # depois que tudo esta em ordem corretamente, isto é, todos os registros invalidos foram substituidos por validos do final, vamos sobreescrever o arquivo com apenas a parte utilizada
        arq.seek(0)
        w = arq.read(posicaoApagar)
        arq.close()

        arq = open("arquivo.txt", 'w') # 'w' pois deseja sobreescrever
        arq.seek(0)
        arq.write(w)
        arq.close()

        print("Arquivo compactado")
        arq.close()

    else:
        print("\nAinda não foi criado nenhum arquivo.\nAntes de realizar compactação, selecione a opção para criar!\n")


    return 0   # se não encontrou a chave ou se o arquivo nao existe
