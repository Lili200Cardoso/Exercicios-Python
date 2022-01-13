real = float(input("Digite o valor que você tem em R$:"))
dolar: float =float( real / 5.26)
print("Você tem U$ {}{:.2f}{} .".format("\033[30;41m",dolar,"\033[m"))