numeros = []
for n in range(0,5):
    numeros.append(int(input(f"Digite um valor para a posição {n+1}:")))
print(f"Você digitou  {numeros}!")
print(f"O Maior valor digitado foi {max(numeros)} nas posições ", end='')
for n, v in enumerate(numeros):
    if numeros[n] == max(numeros):
        print(f"{n+1}...",end='')
print()
print(f"O Menor valor digitado foi {min(numeros)} nas posições ", end='')
for n,v in enumerate(numeros):
    if numeros[n] == min(numeros):
        print(f"{n+1}...",end="")
print()
