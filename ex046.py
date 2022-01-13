from time import sleep
print("\033[31m","===" * 10,"\033[m")
print("\033[31m","     CONTAGEM REGRESSIVA  ","\033[m")
print("\033[31m","===" * 10,"\033[m")

for c in range(10,-1,-1):#start stop step (Start em 10, stop em -1(Quero que termine em 0 mas ele nao lÊ o ultimo numero
    print(c)                         #sendo assim, coloquei o numero anterior a zero(-1)
    sleep(1) #(0.5)meio segundo      #como quero de tras pra frente, usei -1, (se quisesse na ordem normal seria apenas 1)
print("\033[7:33m","     FOGOS DE ARTIFÍCIO!   ","\033[m")

#ACERTEI