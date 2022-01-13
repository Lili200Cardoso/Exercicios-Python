from random import randint#faz a máquina gerar um número aleatorio.
from time import sleep
numero_secreto = randint(0,5)
#print("Pensei no número {}".format(numero_secreto)#para vc saber qual numero random escolheu!
print("-=-" * 20)
print("Vou pensar em número de 0 até 5. Tente adivinhar!!")
print("-=-" * 20)
chute = int(input("em que número eu pensei?"))
print("PROCESSANDO...")
sleep(3)
print("Parabéns! Você conseguiu me vencer!" if chute == numero_secreto else
      "Ganhei!! Eu pensei no número {} "                                                                      
     "e não no {}".format(numero_secreto, chute))#Aqui eu escolhi usar uma condição simplificada!