from time import sleep
n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor:"))
opcao = 0
while opcao != 5:
    print("Escolha uma opção:\n"
          "(1) somar\n"
          "(2) multiplicar\n"
          "(3) maior\n"
          "(4) novos números\n"
          "(5) sair do programa")
    opcao = int(input("Qual a sua opção?"))
    if opcao == 1:
        soma = n1 + n2
        print("A Soma de {} + {} é = {}".format(n1,n2,soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print("O resulatdo de {} x {} é = {}".format(n1,n2,multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        print("Entre o {} e {} o Maior é o {}".format(n1,n2,maior))
    elif opcao == 4:
        print("Digite os novos números:")
        n1 = int(input("Digite um valor:"))
        n2 = int(input("Digite outro valor:"))
    elif opcao == 5:
        print("FINALIZANDO...")
    else:
        print("Opção Invalida, Tente novamente!!")
    print("***" * 10)
    sleep(2)
print("FIM, Volte sempre!!")





