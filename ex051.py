primeiro_termo = int(input("Digite o primeiro termo da sua PA:"))
razao = int(input("Digite a razão de sua PA:"))
decimo = primeiro_termo + (10 - 1) * razao#Aqui eu travei, não sabia o que fazer,formula anotada!

for pa in range(primeiro_termo,decimo + razao,razao):
    print("{} ".format(pa), end="->")
print("Sua PA, tem como primeiro termo {} e razão {}.".format(primeiro_termo, razao))
