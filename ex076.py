print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
tupla = ("sal",2.00,"arroz",28.00,"feijão",8.00)
for pos in range(0,len(tupla)):#Começa na posição zero e vai até o tamanho(len) da lista!
    if pos %2==0:#Se estiver numa posição par...
        print(f"{tupla[pos]:.<15}",end=" ")#:.<15 é formatação(pontos alinhados á esquerda[<])
    else:
        print(f"R${tupla[pos]:>7.2f}")
print("-" * 40)
