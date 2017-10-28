from metodos_basicos import criaArquivo
from metodos_basicos import insere
from metodos_basicos import busca
from metodos_basicos import remove

print("0 - encerrar programa")
print("1 - criar arquivo vazio ou limpar existente")
print("2 - inserir novo registro")
print("3 - buscar um registro")
print("4 - remover um registro")
op = int(input("Digite o que deseja fazer:"))

while(op!=0):
    if op == 1:
        criaArquivo()
    elif op == 2:
        insere()
    elif op == 3:
        ra_busca = input("\nDigite o RA que deseja buscar:")
        registro_encontrado = busca(ra_busca)
        if registro_encontrado != None:
            print("\nDados do registro encontrado:")
            registro_encontrado.exibeRegistro()
            print("\n")

        else:
            print("\nNenhum registro com esse RA foi encontrado")

    elif op == 4:
        ra_busca = input("\nDigite o RA do registro que deseja remover:")
        encontrou = remove(ra_busca)
        if encontrou:
            print("\nRegistro removido com sucesso!")

        else:
            print("\nNenhum registro com esse RA foi encontrado")

    else:
        print("\nOpcao invalida!")

    print("\n0 - encerrar programa")
    print("1 - criar arquivo vazio ou limpar existente")
    print("2 - inserir novo registro")
    print("3 - buscar um registro pelo RA")
    print("4 - remover um registro")
    op = int(input("Digite o que deseja fazer:"))
