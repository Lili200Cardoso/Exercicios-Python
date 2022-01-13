salario = float(input("Digite o valor do seu salario: R$ "))
if salario >= 1250.00:
    print("Seu aumento será de 10%, seu salário será R${:.2f}.".format((salario * 10/100) + salario))
else:
    print("Seu aumento será de 15%, seu salário será R${:.2f}.".format((salario * 15/100) + salario))
    #Também posso usar (salario * 0.10) + salario...me dará o mesmo resultado!