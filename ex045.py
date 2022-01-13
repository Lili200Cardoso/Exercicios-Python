print("\033[1:43m", "@@@" *8, "\033[m")
print("\033[1:43m", "        JOKENPÔ         ", "\033[m")
print("\033[1:43m", "@@@" *8, "\033[m")

opcao = input(("Escolha uma opção:\n"
      "(1) PEDRA\n"
      "(2) TESOURA\n"
      "(3) PAPEL\n"
      "Qual é a sua jogada?\n "))

if opcao == 1 > 2:
    print("PEDRA ganha de TESOURA!")

elif opcao == 2 > 3:
    print("TESOURA ganha de PAPEL")

elif opcao == 3 > 1:
    print("PAPEL ganha de PEDRA")