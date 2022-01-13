n = int(input("Quantos termos você quer mostrar? "))
termo1 = 0
termo2 = 1
print("{} -> {}".format(termo1,termo2),end="")
contador = 3
while contador <= n:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    contador+=1
    print(" -> {}".format(termo3),end="")
print("-> Fim")

