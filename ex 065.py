resposta = "S"
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
while resposta in "Ss":
    n = int(input("Digite um número:"))
    soma = soma + n
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input("Quer continuar? [S/N]")).strip()[0].upper()
media = soma / quantidade
print("Você digitou {} números e a média foi {}.".format(quantidade, media))
print("O Maior valor é {} e o Menor valor é {}.".format(maior, menor))






