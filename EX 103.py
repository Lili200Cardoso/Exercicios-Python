def ficha(j='<desconhecido>',g=0):
    print(f'O jogador {j} fez {g} gols(s) no campeonato!')

nome = str(input('Nome do jogador:'))
gols = str(input(f'Quantos gols o {nome} fez?'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':#strip() é a função que elimina todos os espaços...
    ficha(g=gols)
else:
    ficha(nome,gols)
