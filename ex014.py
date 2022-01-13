celsius = float(input("Digite a temperatura em graus celsius:"))
fahrenheit = celsius * 9 / 5  + 32 #sem necessidade de parenteses, pois a ordem segue a regra de ordem de precedencia.
print("A temperatura {}°c convertida é {}°f.".format(celsius,fahrenheit))
