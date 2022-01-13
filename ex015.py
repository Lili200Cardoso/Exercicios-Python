km = float(input("Quantos Km você andou no carro alugado?"))
dias = int(input("Quantos dias você ficou com o carro alugado?"))
print("Você andou {}km por {} dias,"
      " você gastou R${:.2f} pela quilometragem rodada "
      "e gastou R${:.2f} pelos dias que ficou com o carro,"
      " no total você gastou R${:.2f}.".format(km,dias,km*0.15,dias*60.00,(km*0.15)+ (dias*60.00)))