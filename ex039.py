from datetime import date#colocar data atual

print("\033[7:45m","@@@" * 15,"\033[m")
print("\033[7:45m","           PREVISÃO PARA ALISTAMENTO         ","\033[m")
print("\033[7:45m","@@@" * 15,"\033[m")


ano_atual = date.today().year#chamando a data de hoje!
genero = int(input("Informe seu genero:\n"
               "(1) MASCULINO\n"
               "(2) FEMININO\n"))

if genero == 1:

    ano_nascimento = int(input("Digite o ano do seu nascimento: YYYY"))
    idade = ano_atual - ano_nascimento
    print("Quem nasceu em {} tem {} anos em {}!".format(ano_nascimento,idade,ano_atual))

    if idade == 18:
        print("Está na hora de alistar!")

    elif idade < 18:
        print("Faltam {} anos para se alistar!".format(18 - idade))
        print("Seu alistamento será em {}.".format(ano_atual +(18 - idade)))
    else:
        print("Você já passou do prazo para  se alistar!")
        print("Seu alistamento foi em {}.".format(ano_atual - (idade - 18)))

elif genero == 2:
    print("Você não precisa se alistar!")

