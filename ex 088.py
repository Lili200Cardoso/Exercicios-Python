from random import randint
from time import sleep
lista = []
jogos = []
print("---" * 15)
print("       JOGA NA MEGA SENA       ")
print("---" * 15)
quantidade = int(input("Quantos jogos você quer que eu sorteie?"))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()#coloca em ordem os numeros sorteados
    jogos.append(lista[:])
    lista.clear()
    total+=1
print("---" * 3, f"SORTEANDO {quantidade} JOGOS!", "---" * 3)
for i, l in enumerate(jogos):#ENUMERATE
    print(f"Jogo {i+1}:{l}")
    sleep(2)
print("---" *5, "BOA SORTE!", "---"*5)










