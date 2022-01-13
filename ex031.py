distancia_viagem = float(input("Digite a distancia da sua viagem em Km:"))
print("Você está prestes a começar uma viagem de {} Km". format(distancia_viagem))
if distancia_viagem <=200:
    print("O valor da sua passagem para essa distância será R$ {:.2f}".format(distancia_viagem * 0.50))
else:
    print("O Valor da sua passagem para essa distância será R$ {:.2f}".format(distancia_viagem * 0.45))
#print("