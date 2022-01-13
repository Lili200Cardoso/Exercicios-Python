from random import randint
lista = []
jogos = []
print("___" * 15)
print("    JOGA NA MEGA SENA    ")
print("___" * 15)
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
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print("-=" * 3, f"SORTEANDO {quantidade} JOGOS!", "-=" * 3)
for indice, l in enumerate(jogos):
    print(f"Jogo {indice+1}:{l}")

