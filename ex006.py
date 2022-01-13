n = int(input("Digite um número:"))
print("O Dobro de {}{}{} é igual {}.\n"
      "O triplo é igual {}.\n"
      "E a raiz quadrada é igual {:.2f}.".format("\033[34m",n,"\033[m",n*2,n*3,n**(1/2)))