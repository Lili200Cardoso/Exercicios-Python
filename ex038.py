v1 = int(input("Digite o primeiro valor:"))
v2 = int(input("Digite o segundo valor:"))

if v1 > v2:
    print("O primeiro valor {}, é o  valor {}MAIOR{} !".format(v1,"\033[1:41m","\033[m"))

elif v2 > v1:
    print(" segundo  valor {}, é o {}MAIOR{}!".format(v1,"\033[1:41m","\033[m"))

else:
    print("Não existe valor maior , os dois são {}IGUAIS{}!".format("\033[1:41m","\033[m"))


