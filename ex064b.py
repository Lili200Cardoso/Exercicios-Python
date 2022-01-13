n = contador = soma = 0
n = int(input("Digite um número:[999 para parar]"))
while n != 999:
    soma += n
    contador += 1
    n = int(input("Digite um número:[999 para parar]"))
print("Você digitou {} números,A soma dos numeros digitados é {}".format(contador,soma))
