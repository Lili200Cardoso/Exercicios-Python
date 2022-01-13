while True:
    n = int(input("Quer ver a tabuada de qual número:"))
    if n < 0:
        break
    for contador in range(1,11):
        print(f"{n} x {contador} = {n*contador}")
print("Programa Tabuada Encerrado!")



