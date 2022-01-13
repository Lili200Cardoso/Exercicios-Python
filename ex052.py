n = int(input("Digite um número para sabermos se ele é primo:"))
total_divisivéis = 0
for c in range(1,n+1):
    if n % c == 0:
        print("\033[33m",end='')
        total_divisivéis += 1#++1
    else:
        print("\033[31m",end='' )
    print("{} ".format(c), end='')
print("\n\033[m""O número {} foi divisivel {} vezes".format(n,total_divisivéis))
if total_divisivéis == 2:#Pois numeros primos só podem ser divisivél duas vezes: por 1 e por ele mesmo!
    print("É por isso que ele é PRIMO!")
else:
    print("É por isso que ele NÃO É PRIMO!")