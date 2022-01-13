tupla = ("Zero","um","dois","três","quatro","cinco","seis",
         "sete","oito","nove","dez","onze","doze","treze","quatorze",
         "quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
while True:#loop infinito(Faço isso para que não seja aceito nenhum número fora do intervalo entre 0 e 20)
    numero = int(input("Digite um número entre 0 e 20:"))
    if 0 <= numero <=20:#condição de parada para meu loop
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {tupla[numero]}")



