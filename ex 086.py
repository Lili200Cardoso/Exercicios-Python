matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]#è uma matriz 3x3, coloco zer dentro da
for linha in range(0,3):# submatriz, pra nao precisar usar append para preenche la
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha},{coluna}]: "))
print("==" * 20)
for linha in range(0,3):
    for coluna in range (0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")#:^5formata na impressão
    print()#Esse print, uma identação antes, é  o que faz as matrizes quebrarem de linha!

