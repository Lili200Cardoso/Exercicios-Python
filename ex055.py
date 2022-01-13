maior = 0
menor = 0
for pessoas  in range(1,6):
    peso = float(input("Peso da {}º pessoa:".format(pessoas)))
    if pessoas == 1:
        maior = peso#A primeira pessoa ou o primeiro laço, sempre será o menor peso e tambem o maior peso,#
        menor = peso
        #não existem parametros para comparação!
    else:
        if peso > maior:#entao, criamos os parametros!
            maior = peso
        if peso < menor:
            menor = peso
print("O Maior peso lido foi de {}Kg e o Menor foi {}Kg".format(maior, menor))


