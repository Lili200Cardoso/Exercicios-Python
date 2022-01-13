total = totalmil = menor = contador = 0
barato = " "
while True:
    produto = str(input("Nome do produto:"))
    preco = float(input("Preco do produto R$"))
    contador += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi de R$ {total:.2f}")
print(f"Temos {totalmil} produtos custando mais de R$1.000")
print(f"O produto mais barato foi {barato} que custa R$ {menor:.2f}")