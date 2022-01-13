frase = str(input("Digite uma frase para verificar se ela é um PALÍNDROMO:\n")).strip().upper()
palavras = frase.split()#.split() divide strings, cria uma lista
junto = "".join(palavras)#esse comando com aspas coladinhas serve pra juntas as palavras sem espaço algum!
#esses dois comandos juntos serviram para separar a frase de depois junta las sem espaço!)
inverso = ""#inverte a lista!
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]#len dá o comprimento,-1 == não considera a ultima letra
print("O inverso de {} é {}.".format(junto,inverso))
if junto == inverso:
    print("\033[1:31m","PALÍNDROMO!","\033[m")
else:
    print("Não é um Palíndromo!")

#print("Você digitou a frase {}".format(junto))                   #o segundo -1 ate onde vai,
                                                                 # no caso era ate 0, mas pra mostrar o zero, tenho que
                                                                 # pedir -1;
                                                                 # e o ultimo -1 é porque vai voltando uma letra.

