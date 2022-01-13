n = 0#PODERIA DECLARAR TODAS ESSAS VARIAVEIS EM UMA SÓ LINHA: jÁ QUE TODAS TEM MESMO VALOR:
contador = 0# n = contador = acumulador = 0
acumulador = 0
n = int(input("Digite um número qualquer[999 para parar]:"))
while n != 999:
    acumulador = n + acumulador
    contador+= 1
    n = int(input("Digite um número qualquer[999 para parar]:"))
print("Você digitou {} numeros, a soma desses números é {}.".format(contador, acumulador))


#999 é o flag desse programa(CONDIÇÂO DE PARADA), para que funcione e o mesmo seja desconsiderado enquanto soma, ele deve ser introduzido
#antes do While e no fim, como ultima linha do While!
