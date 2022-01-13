#nome = str(input("Nome:"))
#media = float(input(f"Média de {nome}:"))
#print(f"-Nome é igual a {nome}")
#print(f"-Média é igual a {media}")
#if media < 7:
    #print("-Situação é igual a Recuperação.")
#elif media >= 7:
    #print("-Situação é igual a Aprovado.")
#else:
    #print("-Situação è igual a Reprovado.")
aluno = {}
aluno['Nome'] = str(input("Nome: "))
aluno['Media'] = float(input(f"Média de {aluno['Nome']}: "))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5<= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print("_" * 25)
for k, v in aluno.items():
    print(f"{k} é igual a {v}.")




