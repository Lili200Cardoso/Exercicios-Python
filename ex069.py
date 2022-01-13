contador = homem = mulher= 0
resposta = "Ss"
while resposta in  "Ss":
    print("___" * 10)
    print("    CADASTRE UMA PESSOA    ")
    print("___" * 10)
    idade = int(input("Idade:"))
    sexo = str(input("Sexo : [M/F]")).upper()[0].strip()
    resposta= str(input("Quer continuar: [S/N]")).upper()[0].strip()
    if idade >= 18:
        contador += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher += 1
print(f" Tivemos {contador} pessoas com mais de 18 anos!")
print(f" Foram {homem} Homens foram cadastrados!")
print(f"Tivemos {mulher} mulheres com menos de 20 anos!")

