salario = float(input("Digite o valor do salario R$"))
novo_salario = salario + (salario * 0.15) #podendo também usar "(salario * 15/100)"
print("O novo salário, com 15% de aumento, é R$ {:.2f}".format(novo_salario))