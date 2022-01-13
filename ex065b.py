resposta = "S"
soma = 0
contador = 0
media = 0
maior = menor = 0
while resposta in "Ss":
    n = int(input("Digite um número:"))
    soma = soma + n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input("Quer continuar?[S/N]")).upper().strip()[0]
media = soma / contador
print("Você digitou {} numeros, a soma deles é {}, e a média é {}.".format(contador,soma,media))
print("O maior foi {} e o menor foi {}.".format(maior, menor))


