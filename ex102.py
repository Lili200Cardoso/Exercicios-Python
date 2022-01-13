def fatorial(n,show=False):
    """
    -> CALCULA O FATORIAL DE UM NÚMERO.
    :param n: O NÚMERO Á SER CALCULADO
    :param show: (OPCIONAL) MOSTRA OU NÃO O CALCULO FEITO!
    :return:O VALOR DO fATORIAL DE UM NÚMERO(N)
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c > 1:
                print('x',end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f



n = int(input('Digite um número:'))
print(fatorial(n,show=True))