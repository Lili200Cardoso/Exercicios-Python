print("\033[7:34m","-*-" * 15,"\033[m")
print("\033[7:34m","           ANALISADOR DE TRIANGULOS          ","\033[m")
print("\033[7:34m","-*-" * 15,"\033[m")

r1 = float(input("Digite o tamanho da primeira reta:"))
r2 = float(input("Digite o tamanho da segunda reta:"))
r3 = float(input("Digite o tamanho da terceira reta:"))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:#CADA UM DOS SEGMENTOS
    print("Com essas medidas você conseguira formar um triangulo ", end='')
    if r1 == r2 and r2 == r3:
        print("\033[7:34m", "EQUILÁTERO", "\033[m\n"
               "Todos os lados são iguais!")
    elif r1 == r2 or r1 == r3:
        print("\033[7:34m","ISÓSCELES","\033[m\n"
                "Dois lados iguais")
    else: #r1 != r2 and r1 != r3:
        print("\033[7:34m","ESCALENO","\033[m\n"
                "Todos os lados diferentes!")
else:
    print("Com essas medidas é IMPOSSIVEL formar um triangulo!")