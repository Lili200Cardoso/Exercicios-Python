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


n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')

