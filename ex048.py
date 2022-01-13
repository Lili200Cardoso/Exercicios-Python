s = 0 #acumulador(algo que você tenha que somar,guardar)
cont = 0 #contador sempre soma com + 1
for c in range(1,501,2):
    if c % 3 == 0:
        #if c % 2 == 1:
        s = s + c#aqui estou acumulando todos os numeros que aparecem...(SOMANDO)
        cont = cont + 1 #ou cont += 1
print("O Somatorio de todos os  {} valores é {}{}{}".format(cont,"\033[1:35m",s,"\033[m"))



#ACERTEI