contador  = soma = quantidade = menor = 0
barato = " "
resposta = "Ss"
while resposta in "Ss":
    produto = str(input("Digite o nome do produto:")).upper().strip()
    preco = float(input("Digite o preço do produto:R$ "))
    resposta = str(input("Quer continuar?[S/N]")).upper()[0].strip()
    contador += 1
    soma += preco
    if preco > 1000.00:
         quantidade += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
print(f"O Total da compra foi R$ {soma:.2f}.")
print(f"Temos {quantidade} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custou R$ {menor:.2f}")


