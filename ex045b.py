from random import randint
from time import sleep
itens = ("PEDRA","PAPEL","TESOURA")
computador = randint(0,2)#sequência da lista de itens(0,1,2)==(pedra, papel, tesoura)
#print("O computador escolheu {}".format(itens[computador]))     #Só para verificação!!
print("Suas opções:\n"
      "\033[1:41m","  [0] PEDRA   ","\033[m\n",
      "\033[1:41m"," [1] PAPEL   ","\033[m\n",
      "\033[1:41m"," [2] TESOURA ","\033[m\n")
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
print("\033[1:31m","-=" * 12,"\033[m")
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("\033[1:31m","-=" * 12,"\033[m")

if computador == 0:#computador jogou pedra
    if jogador == 0:
        print("\033[1:31m","EMPATE","\033[m")
    elif jogador == 1:
        print("JOGADOR GANHOU!")
    elif jogador == 2:
        print("COMPUTADOR GANHOU!")
    else:
        print("Jogada invalida")
elif computador == 1:#computador jogou papel
    if jogador == 0:
        print("JOGADOR GANHOU!")
    elif jogador == 1:
        print("\033[1:31m","EMPATE","\033[m")
    elif jogador == 2:
        print("COMPUTADOR GANHOU!")
    else:
        print("Jogada invalida")
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print("JOGADOR GANHOU!")
    elif jogador == 1:
        print("COMPUTADOR GANHOU!")
    elif jogador == 2:
        print("\033[1:31m","EMPATE","\033[m")
    else:
        print("Jogada invalida")