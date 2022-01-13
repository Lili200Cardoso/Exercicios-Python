expressao = str(input("Digite uma expressão para analisarmos se é válida:"))
parenteses = []
for simbolo in expressao:
    if simbolo == "(":
        parenteses.append("(")
    elif simbolo == ")":
        if len(parenteses) > 0:
            parenteses.pop()#pop remove o último elemento da lista
        else:
            parenteses.append(")")
            break
if len(parenteses) == 0:
    print("Sua expressão esta válida!")
else:
    print("Sua expressão não é válida!")
    