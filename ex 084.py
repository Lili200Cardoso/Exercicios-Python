provisoria = []
definitiva = []
maior = menor = 0
while True:
    provisoria.append(str(input("Nome:")))
    provisoria.append(float(input("Peso:")))
    if len(definitiva) == 0:
        maior = menor = provisoria[1]#indice 1 um provisoria trata se do peso das pessoas.
    else:
        if provisoria[1] > maior:
            maior = provisoria[1]
        if provisoria[1] < menor:
            menor = provisoria[1]
    definitiva.append(provisoria[:])
    provisoria.clear()
    opcao= str(input("Quer continuar: [S/N]")).upper()
    if opcao in "Nn":
        break
print("***" * 10)
print(f"Ao todo vc cadastrou {len(definitiva)} pessoas.")
print(f"O maior peso foi de {maior}KG, peso de ", end="")
for pessoa in definitiva:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end="")
print()
print(f"O menor peso foi de {menor}KG ,peso de ", end="")
for pessoa in definitiva:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]",end="")
print()


