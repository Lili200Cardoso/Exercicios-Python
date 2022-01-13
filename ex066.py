contador = soma  = 0
while True:
    n = int(input("Digite um número: (999 para parar)"))
    if n == 999:
        break
    soma += n
    contador += 1
print(f"Você digitou {contador} números e a soma deles é {soma}.")
