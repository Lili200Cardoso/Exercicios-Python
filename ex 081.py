numero = list()
while True:
    numero.append(int(input("Digite um valor:")))
    opcao = str(input("Quer continuar?[S/N]")).upper()
    if opcao in "Nn":
        break
print("-=" * 25)
print(f"Você digitou {len(numero)} elementos.")
numero.sort(reverse = True)
print(f"Os valores em ordem decrescente são: {numero}")
if 5 in numero:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")

