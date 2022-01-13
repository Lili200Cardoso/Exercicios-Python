n1 = int(input("Entre com um valor:"))
n2 = int(input("Entre com um segundo valor:"))
opcao = 0
while opcao !=5:
    print("[1] somar\n"
    "[2] multiplicar\n"
    "[3] maior\n"
    "[4] novos números\n"
    "[5] sair do programa\n")
    opcao = int(input("Selecione a sua opção:"))
    if opcao == 1:
        soma = n1 + n2
        print("O número {} + o número {} é igual á {}.".format(n1,n2,soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print("O número {} multiplicado pelo número {} é igual á {}.".format(n1,n2,soma))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print("O número {} é o maior!".format(maior))
        else:
            maior = n2
            print("O número {} é o maior".format(maior))
    elif opcao == 4:
        print("Informe os novos numeros:")
        n1 = int(input("Digite um novo valor:"))
        n2 = int(input("Digite outro novo valor:"))
    elif opcao == 5:
        print("FInalizando...")
    else:
        print("Opção inválida!Tente novamente!!")
print("FIM")