s = 0#acumulador
for c  in range(1,7):
    n = int(input("Digite o {}º valor:".format(c)))
    if n % 2 == 0:
        s = n + s#s += n
print("O somatorio entre todos os valores pares é {}{}{}".format("\033[7:46m",s,"\033[m"))


#ACERTEI