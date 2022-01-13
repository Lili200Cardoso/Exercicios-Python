sexo = int(input("Selecione seu sexo:\n"
                 "[1] Masculino\n"
                 "[2] Feminino\n"))
while sexo > 2:
     sexo = int(input("Opção Inválida, tente novamente:\n"
                     "Selecione seu sexo:\n"
                     "[1] Masculino\n"
                     "[2] Feminino\n"))

print("Sua opção sexual a é {} .Opção selecionada com sucesso!".format(sexo))



