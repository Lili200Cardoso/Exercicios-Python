temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input("Nome:")))
    temporario.append(float(input("Peso:")))
    if len(principal) == 0:
        maior = menor = temporario[1]#temporario[1], trata se do peso.
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])#A lista principal copia a lista temporaria[:]
    temporario.clear()#A lista temporaria é apagada, para não replicar na impressão.
    resposta = str(input("Quer continuar? [S/N]"))
    if resposta in "Nn":
        break
print("++" * 20)
print(f"Ao todo você cadastrou {len(principal)} pessoas")
print(f"O maior peso foi de {maior}Kg. Peso de ",end="")
for pessoa in principal:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end="")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ",end="")
for pessoa in principal:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end="")
print()