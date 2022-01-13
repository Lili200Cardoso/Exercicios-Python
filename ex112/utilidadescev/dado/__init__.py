def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()#replace(),substitui, nocaso a virgula por ponto final.
        if entrada.isalpha() or entrada == '':#isalpha() pergunta se é alphanúmerico...
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

def leiaInt(msg):
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!Digite um número inteiro válido.\033[m')
        if ok:
            break
    return num

