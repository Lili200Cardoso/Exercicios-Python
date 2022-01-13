from random import randint
v = 0
print("=-" * 15)
print(" VAMOS JOGAR PAR OU ÍMPAR? ")
print("=-" * 15)
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = computador + jogador
    opcao = " "
    while opcao is not "PpIi":
        opcao= str(input("Par ou Ímpar?[P/I]")).upper()[0].split()
    if opcao == "P":
        if total % 2 == 0:
            print("Você GANHOU!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif opcao == "I":
        if total % 2 == 1:
            print("Você GANHOU")
            v += 1
        else:
            print("Você perdeu!")
            break
    print(f"Você jogou {jogador} e o computador jogou {computador}.Total é {total}")
print(f"GAME OVER, você ganhou {v} vezes!")