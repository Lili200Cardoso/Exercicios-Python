primeiro_termo = int(input("Digite o primeiro termo da sua PA:"))
razao = int(input("Digite a razão de sua PA:"))
contador = 1
termos = primeiro_termo
while contador  <= 10:
    print("{} ".format(termos), end="->")
    termos = termos + razao
    contador += 1
print("Sua PA, tem como primeiro termo {} e razão {}.".format(primeiro_termo, razao))