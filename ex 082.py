numero = list()
pares = list()
impares = list()
while True:
    numero.append(int(input("Digite um número:")))
    opcao = str(input("Quer continuar? [S/N]")).upper()
    if opcao in "Nn":
        break
for indice, valor in enumerate(numero):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print("++" * 20)
print(f"A lista completa é {numero}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
