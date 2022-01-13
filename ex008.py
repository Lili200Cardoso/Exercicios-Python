metros = float(input("Digite uma medida em metros para ser convertida em centimetros e em milimetros:"))
print("A medida de {}{}{}m  é  {:.0f}cm  e  {:.0f}mm".format("\033[36m",metros,"\033[m",metros*100, metros*1000))
