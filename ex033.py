n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
#if n1 > n2 and n1 > n3:
    #print("O número maior é {}".format(n1))
#elif n2 > n1 and n2 > n3:
    #print("O número maior é {}".format(n2))
#else:
    #print("O número maior é {}".format(n3))
    #if n1 < n2 and n1 < n3:
        #print("O número menor é {}".format(n1))
    #elif n2 < n3 and n2 < n1:
        #print("O número menor é {}".format(n2))
    #else:
        #print("O número menor é {}".format(n3))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))
#Essa solução foi do professor, a minha está como comentário!