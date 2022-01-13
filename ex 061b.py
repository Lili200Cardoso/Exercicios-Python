primeiro_termo = int(input("Digite o primeiro termo da sua PA:"))
razao = int(input("Digite a razão da sua PA:"))
pa = primeiro_termo
contador= 0
while contador <= 10:
    print("{} -> ".format(pa), end=" ")
    pa = pa + razao
    contador += 1
print("FIM")

