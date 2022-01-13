largura = float(input("Digite a largura da área:"))
altura = float(input("Digite a altura da área:"))
area = altura * largura
tinta = area / 2
print("Você vai gastar numa área de {}{}{}metros quadrados,"
      " {:.2f}litros de tinta.".format("\033[42;34m",area,"\033[m",tinta))
