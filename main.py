# Organização e Recuperação da Informação - Turma A.
# TRABALHO 1 - Implementação de arquivo sem ordenação.
    # Isadora Eliziário Gallerani - 726542 
    # Renata Sarmet Smiderle Mendes - 726586 

from metodos_basicos import criaArquivo
from metodos_basicos import insere
from metodos_basicos import busca
from metodos_basicos import remove
from metodos_basicos import listagem
from metodos_basicos import compactacao

# menu de opcoes para o usuario
print("0 - encerrar programa")
print("1 - criar arquivo vazio ou limpar existente")
print("2 - inserir novo registro")
print("3 - buscar um registro")
print("4 - remover um registro")
print("5 - listar todos os registros")
print("6 - realizar compactacao")
print("7 - inserção em lote")
op = int(input("Digite o que deseja fazer:"))

# as entradas serao fornecidas pelo usuario
while(op!=0):       # opcao 0 - encerra o programa
    if op == 1:     # opcao 1 - cria o arquivo vazio ou limpa existente
        criaArquivo()
    elif op == 2:   # opcao 2 - insere novo registro
        insere()
    elif op == 3:   # opcao 3 - busca por registro sera realizada atraves da chave - o RA
        ra_busca = input("\nDigite o RA que deseja buscar:")
        registro_encontrado = busca(ra_busca)       # procura o RA fornecido pelo usuario
        if registro_encontrado != None:             # encontrando o RA, fornece o registro
            print("\nDados do registro encontrado:")
            registro_encontrado.exibeRegistro()

        else:       # caso nao encontre o RA, consequentemente nao foi encontrado um registro correspondente
            print("\nNenhum registro com esse RA foi encontrado")

    elif op == 4:       # opcao 4 - remocao de registro
        ra_busca = input("\nDigite o RA do registro que deseja remover:")
        encontrou = remove(ra_busca)        # procura pelo RA fornecido
        if encontrou:
            print("\nRegistro removido com sucesso!")       # encontrado o RA, remove-se o registro

        else:       # RA nao encontrado, consequentemente nao foi encontrado registro correspondente 
            print("\nNenhum registro com esse RA foi encontrado")

    elif op == 5:       # opcao 5 - listagem de registros
        print("\nRegistros salvos:\n")
        listagem()      # exibe todos os registros salvos
    elif op == 6:       # opcao 6 - compactacao
        compactacao()
    elif op == 7:       # opcao 7 (extra) - insercao em lote
        n = int(input("\nDigite quantas inserções deseja fazer:"))
        for i in range(0,n):
            insere()        # insere registros de acordo com a quantidade de insercoes fornecidas
    else:
        print("\nOpcao invalida!")      # outra opcao diferente digitada, acusa-se invalidez 

    print("\n0 - encerrar programa")
    print("1 - criar arquivo vazio ou limpar existente")
    print("2 - inserir novo registro")
    print("3 - buscar um registro pelo RA")
    print("4 - remover um registro")
    print("5 - listar todos os registros")
    print("6 - realizar compactacao")
    print("7 - inserção em lote")
    op = int(input("Digite o que deseja fazer:"))
