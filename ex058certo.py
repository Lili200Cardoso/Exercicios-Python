from random import randint
computador = randint(0,10)
print("Sou seu computador...Acabei de pensar em um número entra 0 e 10!"
      "Será que você consegue adivinhar qual foi?")
acertou = False#acertou é falso porque o jogador ainda não acertou
palpites = 0#palpites é zero porque ainda não houve palpite nenhum...(Aideia é contabilizar a quantidade de palpites)
while not acertou:
    jogador = int(input("Qual é o seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez!")
        elif jogador > computador:
            print("Menos...Tente mais uma vez!")
print("Acertou com {} tentativas, PARABÉNS!!".format(palpites))
