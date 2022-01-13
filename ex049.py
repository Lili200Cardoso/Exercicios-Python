n = int(input("Digite um número para saber a tabuada do mesmo:"))
print("\033[31m","@" * 15,"\033[m")
print("\033[31m"," TABUADA DE {} ".format(n),"\033[m")
print("\033[31m","@" * 15,"\033[m")

for c in range(0,11):
    print("{} x {} = {}".format(n,c,n * c))



#ACERTEI