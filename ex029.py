velocidade = float(input("Escreva a velocidade atual  do seu carro:"))
if velocidade > 80:
    print("Você foi MULTADO!Você excedeu o limite que é 80Km/h.")
    print("Você pagará de multa R${:.2f}".format( (velocidade - 80) * 7.00))
else:
    print("Velocidade dentro do limite!Boa Viagem!")
