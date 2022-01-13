n = int(input("Digite um número para saber o seu fatorial:"))
contador = n
fatorial = 1
while contador > 0:
    print("{}  ".format(contador), end=' ')
    print("x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1
print("O fatorial de {} será {}".format(n,fatorial))
