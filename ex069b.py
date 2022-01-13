total18= homem = mulher20= 0
while True:
    idade = int(input("Idade:"))
    sexo =" "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade >=18:
        total18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {total18}")
print(f"Ao todo foram {homem} homens cadastrados!")
print(f"E temos {mulher20} mulheres com menos de 20 anos!")


