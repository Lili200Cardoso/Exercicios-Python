print("\033[7:45m","===" * 10,"\033[m")
print("\033[7:45m","           CONVERSOR          ","\033[m")
print("\033[7:45m","===" * 10,"\033[m")

numero = int(input("Digite um número para ser convertido:"))

print("Escolha uma opçao para sua Conversão:\n"
      "(1) Binário\n"
      "(2) Octal\n"
      "(3) Hexadecimal\n")

opção = int(input("Sua opção:"))

if opção == 1:
      print("{} convertido para BINÁRIO é igual á {}".format(numero,bin(numero)[2:]))#[:2] usando isso, estou dizendo que
      #quero que comece a mostras da segunda posição em diante, para que não seja visto 0b ou 0x ou 0o;

elif opção == 2:
      print("{} convertido para OCTAL é igual á {}".format(numero, oct(numero)[2:]))

elif opção == 3:
      print("{} convertido pra HEXADECIMAL é igual {}".format(numero, hex(numero)[2:]))

else:
      print("Essa opção não existe!")


#if 1 == numero.bin():
      #print("O Binário de {} é {}".format.bin(numero))