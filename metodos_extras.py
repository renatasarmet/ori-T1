# Metodo que garante que a string passada tenha o tamanho desejado
# Para isso, se o tamanho da string for menor que o tamanho desejado, preenche com "_"
# Se for maior, retorna apenas a parte que cabe no tamanho desejado
# Se for igual, deixa como está
# Parametro: string que deseja garantir o tamanho; e tam, tamanho que deseja que a string possua
# Retorno: string com o tamanho correto
def tamanhoCorreto(string, tam):
    # garantindo que o dado seja string
    string = str(string)

    # garantindo que o dado armazenado seja do tamanho correto
    size = len(string.encode('utf-8'))
    while(size < tam):      # sobrando tamanho no campo, este sera preenchido com '_' para cada byte que faltar
        string += '_'
        size = len(string.encode('utf-8'))

    string = string[:tam]   # pega os primeiros tam caracteres
    return string
