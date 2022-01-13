from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas  in range(1,8):
    ano_nascimento = int(input("em que ano a {}º pessoa nasceu?".format(pessoas)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print("Ao todos tivemos {} pessoas maiores de idade e "
      "{} pessoas menores de idade".format(total_maior, total_menor))
