nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f} , a média do aluno é {:.1f}".format(nota1, nota2, media))

if media < 5:
    print("\033[1:34m","REPROVADO","\033[m\n")

elif (media == 5) or (media <= 6.9):
    print("\033[1:34m", "RECUPERAÇÃO", "\033[m\n")

else:
    print("\033[1:34m", "APROVADO", "\033[m\n")


