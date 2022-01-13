frase = str(input("Digite uma frase para verificar se ela é um PALÍNDROMO:\n")).strip().upper()
palavras = frase.split()#.split() divide strings, cria uma lista
junto = "".join(palavras)
inverso = junto[::-1]#usando fatiamento de strings:[::-1],sem inicio, sem fim e diminuindo de 1 em 1;
print("O inverso de {} é {}.".format(junto,inverso))
if junto == inverso:
    print("\033[1:31m","PALÍNDROMO!","\033[m")
else:
    print("Não é um Palíndromo!")