def tamanhoCorreto(string, tam):
    #Garantindo que o dado seja string
    string = str(string)

    #Garantindo que o dado armazenado seja do tamanho correto
    size = len(string.encode('utf-8'))
    while(size < tam):
        string += '_'
        size = len(string.encode('utf-8'))

    string = string[:tam]
    return string
