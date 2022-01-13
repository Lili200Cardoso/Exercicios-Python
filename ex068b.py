from random import randint
venceu = 0
while True:
    jogador = int(input("Diga um valor:"))
    computador = randint(0,10)
    total = jogador + computador
    opcao = " "
    while opcao not in "PpIi":
        opcao = str(input("Par ou Ímpar [P/I]: ")).upper()[0].strip()
    print(f"Você jogou {jogador} e o computador jogou {computador}.Total de {total}")
    if opcao == "P":
        if total % 2 == 0:
            print("Você VENCEU!!")
            venceu += 1
        else:
            print("Você Perdeu!")
            break
    elif opcao == "I":
        if total % 2 == 1:
            print("VocÊ VENCEU!")
            venceu += 1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER!Você venceu {venceu} vezes.")