n = int(input("Digite um número para ser fatorado:"))
fatorial = n
n = n-1
for n in range(n, 0, -1):
    valorFatorial = fatorial
    fatorial = fatorial * n
    print("{} x {} = {}".format(valorFatorial,n, fatorial))

