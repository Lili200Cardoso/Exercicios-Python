from datetime import date
ano = int(input("Que ano você quer analisar: Coloque 0 para analisar o ano atual:"))
if ano == 0:
    ano = date.today().year#comando para colocar a data atual, no caso ano!
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#O ano deve ser divisivel por 4 e por 400;
    print(" {} É um ano BISSEXTO!".format(ano))
else:
    print(" {} Não é um ano bissexto!".format(ano))