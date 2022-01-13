print("***" *10)
print("   SEQUÊNCIA FIBONACCI   ")
print("***" * 10)
n = int(input("Quantos termos você quer mostrar?"))
termo1 = 0
termo2 = 1
print("~" * 30)
print("{} -> {}".format(termo1,termo2), end='')
contador = 3#porque o primeiro e o segundo termo eu já sei!
while contador <= n:
    termo3 = termo1 + termo2
    print(" -> {}".format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    contador+= 1
print("-> FIM")
print("~" * 30)
