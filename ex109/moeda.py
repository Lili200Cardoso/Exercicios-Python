def aumentar(preco=0,taxa=0,format=False):
    """
    ->AUMENTA O UM VALOR
    :param preco: VALOR
    :param taxa: PORCENTAGEM QUE IRÁ AUMENTAR NO CASO AQUI SERÁ 10%
    :param format: PARA FORMARTAR O TIPO DE MOEDA, NO CASO, R$!
    :return: O CALCULO FORMATO!
    """
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preco=0,taxa=0,format=False):
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)

def dobro(preco=0,format=False):
    res = preco * 2
    return res if not format else moeda(res)

def metade(preco=0,format=False):
    res = preco / 2
    return res if not format else moeda(res)

def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:>5.2f}'.replace('.',',')#replace(),substituiu um item por outro.
              #>8.2F(fORMATAÇÃO:00.00 ALINHADO A DIREITA)                               #No caso substitui o ponto por virgula.