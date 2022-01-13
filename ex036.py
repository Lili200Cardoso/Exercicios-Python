print("\033[7:40:31m","XXX" * 9,"\033[m" )
print("\033[7:40:31m","  SIMULADOR DE EMPRÉSTIMO  ","\033[m" )
print("\033[7:40:31m","XXX" * 9,"\033[m")
print("SEJA BEM VINDO AO SEU SIMULADOR PESSOAL")

casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o valor do seu salário R$ "))
anos = int(input("Em quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
print("Para pagar uma casa de R$ {:.2f} em {} anos".format( casa,anos))
print("A prestação será de R$ {:.2f}".format(prestacao))
minimo = salario * 30/100


if prestacao >= minimo:
    print("IMPRÉSTIMO REPROVADO")
    print("Prestação excedeu 30% do salário!"
          "Você deveria pagar em {} prestaçoes de R$ {:.2f} !".format(anos, prestacao))
else:
    print("IMPRÉSTIMO APROVADO, PARABÉNS!!")
    print("Você deverá pagar em {} prestaçoes de R$ {:.2f} !".format(anos, prestacao))


