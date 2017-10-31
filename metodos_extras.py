def tamanhoCorreto(string, tam):
    # garantindo que o dado seja string
    string = str(string)

    # garantindo que o dado armazenado seja do tamanho correto
    size = len(string.encode('utf-8'))
    while(size < tam):      # apos ler a entrada, sobrando tamanho no campo, este sera preenchido com '_' para cada byte que faltar
        string += '_'
        size = len(string.encode('utf-8'))

    string = string[:tam]
    return string
