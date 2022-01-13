print("\033[1:35m","%%%" * 15, "\033[m")
print("\033[1:35m","            CALCULADORA IMC     ", "\033[m")
print("\033[1:35m","%%%" * 15, "\033[m")

peso = float(input("Digite o seu peso: (kg)"))
altura = float(input("Digite sua altura: (m)"))

imc = peso / (altura * altura)# OU PESO / (ALTURA ** 2)
print("O IMC é {:.1f}".format(imc))

if imc < 18.50:
    print("\033[1:35m", "Abaixo do Peso", "\033[m")

elif 18.50<= imc < 25:
    print("\033[1:35m", "Peso Normal", "\033[m")

elif 25 <= imc < 30:
    print("\033[1:35m", "Sobrepeso", "\033[m")

elif imc == 40:
    print("\033[1:35m", "Obesidade", "\033[m")

else:
    print("\033[1:35m", "Obesidade Mórbida, CUIDADO!", "\033[m")
