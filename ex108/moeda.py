def aumentar(preco=0,taxa=0):
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco=0,taxa=0):
    res = preco - (preco * taxa/100)
    return res

def dobro(preco=0):
    res = preco * 2
    return res

def metade(preco=0):
    res = preco / 2
    return res

def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:>5.2f}'.replace('.',',')#replace(),substituiu um item por outro.
              #>8.2F(fORMATAÇÃO:00.00 ALINHADO A DIREITA)                               #No caso substitui o ponto por virgula.