primeiro_termo = int(input("Digite o primeiro termo da sua PA:"))
razao = int(input("Digite a razão da sua PA:"))
pa = primeiro_termo
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print("{} -> ".format(pa), end=" ")
        pa = pa + razao
        contador += 1
    print("PAUSA...")
    mais = int(input("Quantos termos você quer mostrar a mais?"))
print("Progressão Aritmética com {} termos mostrados.".format(total))





