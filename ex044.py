print("\033[1:45m","&&&" * 10,"\033[m")
print("\033[1:45m","      SIMULADOR DE COMPRAS    ","\033[m")
print("\033[1:45m","&&&" * 10,"\033[m")

preco = float(input("Digite o preço das compras:"))
condicao_pagamento = int(input("Escolha como quer pagar o produto:\n"
                          "(1) á vista dinheiro ou cheque: 10% desc.\n"
                          "(2) á vista no cartão: 5% desc.\n"
                          "(3) até 2x no cartão: Preço Normal\n"
                          "(4) 3x ou mais no cartão: 20% de juros:\n"
                               "Qual a sua opção?\n"))

if condicao_pagamento == 1:
    novo_preco = preco - (preco * 10/100)
    #print("O valor do seu produto será de R${} {:.2f}{}".format("\033[1:45m",novo_preco,"\033[m"))

elif condicao_pagamento == 2:
    novo_preco = preco - (preco * 5/100)


elif condicao_pagamento == 3:
    novo_preco = preco
    parcela = novo_preco / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))

elif condicao_pagamento == 4:
    novo_preco = preco + (preco * 20/100)
    total_parcelas = int(input("Quantas parcelas?"))
    parcela = novo_preco / total_parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} SEM JUROS".format(total_parcelas,parcela))

else:
    novo_preco = preco
    print("\033[1:45m","OPÇÃO INVALIDA","\033[m")
print("Sua compra de R$ {}{:.2f}{}, vai custar R${:.2f} no final.".format("\033[1:45m",preco,"\033[m",novo_preco))


