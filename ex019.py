import random #from random import choise
aluno1 = input("Digite o nome do primeiro aluno:")
aluno2 = input("Digite o nome do segundo aluno:")
aluno3 = input("Digite o nome do terceiro aluno:")
aluno4 = input("Digite o nome do quarto aluno:")
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)#choise é função do random;Poderia ser"escolhido = choise(lista)"
print("O Aluno sorteado foi {}".format(escolhido))
#esse exercicio eu não soube resolver...
