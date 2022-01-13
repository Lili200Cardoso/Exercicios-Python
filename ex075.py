numero = (int(input("Digite o primeiro valor:")),#tupla
        int(input("Digite o segundo valor:")),
        int(input("Digite o terceiro valor:")),
        int(input("Digite o último valor:")))
print(f"Você digitou os valores {numero}")
print(f"O número 9 apareceu {numero.count(9)} vezes")
if 3 in numero:
    print(f"O primeiro valor 3 foi digitado na {numero.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print(f"Os valores pares digitados foram: ", end=" ")
for n in numero:
    if n % 2 == 0:
        print(n,end='  ')

