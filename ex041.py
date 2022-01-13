from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano do seu nascimento:"))
idade_atleta = ano_atual - ano_nascimento
print("Sua idade é {} anos, VOCÊ É UM ATLETA:".format(idade_atleta))

if idade_atleta <= 9:
    print("\033[1:34m","MIRIM","\033[m")

elif idade_atleta <= 14:
    print("\033[1:34m", "INFANTIL", "\033[m")

elif idade_atleta <= 19:
    print("\033[1:34m", "JUNIOR", "\033[m")

elif idade_atleta  <= 25:
    print("\033[1:34m", "SÊNIOR", "\033[m")

else:
    print("\033[1:34m", "MASTER", "\033[m")

