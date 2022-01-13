from datetime import datetime#Coloca a data atual do computador
cadastro = {}
cadastro['Nome'] = str(input("Nome:"))
nascimento = int(input("Ano de Nascimento:"))
cadastro['Idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input("Carteira de Trabalho(0 Não tem):"))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input("Ano de contratação:"))
    cadastro['Salário'] = float(input("Salário:"))
    cadastro['Aposentadoria'] = cadastro['Idade']+((cadastro['Contratação'] + 35) - datetime.now().year )
print("-=" * 20)
for k, v in cadastro.items():
    print(f"{k} tem o valor {v}.")