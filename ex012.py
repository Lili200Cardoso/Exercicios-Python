preco = float(input("Digite o preço do produto R$"))
novo_preco = preco - (preco * 0.05) #poderia também usar "(preco * 5/100)"
print("O novo preço do produto é R$ {}{:.2f}{}".format("\033[7;41;30m",novo_preco,"\033[m"))
