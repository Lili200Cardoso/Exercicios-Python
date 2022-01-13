somaidade = 0#Declaramos as variavéis que vamos usar dentro de um for, pelo lado de fora do for!
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totalmulher20 = 0
for pessoas  in range(1,5):
    print("------{}ºPESSOA------".format(pessoas))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade = somaidade + idade# ou somaidade+=idade
    if pessoas == 1 and sexo in "Mm":#se a primeira pessoa for do sexo masculino
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade desse grupo é de {} anos.".format(mediaidade))
print("O Homem mais velho tem {} anos e o nome dele é {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos!".format(totalmulher20))