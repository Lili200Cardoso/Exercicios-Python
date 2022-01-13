numero = list()
while True:
    n=int(input("Digite um valor:"))
    if n not in numero:
        numero.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor Duplicado, Não vou adicionar!")
    opcao = str(input("Quer continuar?[S/N]:")).upper()
    if opcao in "Nn":
        break
print("-=" * 20)
numero.sort()
print(f"Você digitou {numero}")
