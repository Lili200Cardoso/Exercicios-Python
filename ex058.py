from random import randint
computador = randint(0,10)
print("Olá, sou seu computador...\n"
      "Estou pensando em um número,\n"
      "Será que você consegue adivinhar?!")
tentativas = 0
acertou = False

while not acertou:
    jogador = int(input("Qual o seu palpite?\n"))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos...")
        elif jogador < computador:
            print("Mais...")
print("Você acertou com {} tentativas!Parabéns!!".format(tentativas))






