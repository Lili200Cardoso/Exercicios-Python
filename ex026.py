frase = str(input("Digite uma frase qualquer:")).upper().strip()#upper para Maiusculas, strip para eliminar espacos vazios
print("A letra A aparece {} vezes nesta frase".format(frase.count('A')))#count para contar quantos existem
print("A primeira letra a apareceu na posição {}".format(frase.find('A')))
print("A ultima letra A apareceu na posição {}".format(frase.rfind('A')))#rfind, contar até ao final da string.
