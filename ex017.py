cateto1 = float(input("Digite o comprimento do cateto oposto de um triangulo retângulo:"))
cateto2 = float(input("Digite o comprimento do cateto adjacente de um triangulo retângulo:"))
hipotenusa = (cateto1*cateto1) + (cateto2*cateto2)#ou (cateto1 ** 2 + cateto2 ** 2) ** (1/2)
print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa**(1/2)))
#ou posso fazer assim:
#import math
#cateto1 = float(input("Digite o comprimento do cateto oposto:"))
#cateto2 = float(input("Digite o comprimento do cateto adjacente:"))
#hipotenusa = math.hypot(cateto1, cateto2)
#print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))

