print("-*-" * 20)
print("ANALIZADOR DE TRIANGULOS")
print("-*-" * 20)
r1 = float(input("Digite o tamanho da primeira reta:"))
r2 = float(input("Digite o tamanho da segunda reta:"))
r3 = float(input("Digite o tamanho da terceira reta:"))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:#CADA UM DOS SEGMENTOS
    print("Com essas medidas você conseguira formar um triangulo")
else:
    print("Com essas medidas é impossivel formar um triangulo!")