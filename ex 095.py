jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador:"))
    total = int(input(f"Digite quantos jogos {jogador['nome']} jogou?"))
    partidas.clear()
    for cont in range(0,total):
        partidas.append(int(input(f"Quantos gols na partida {cont + 1}?")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opcao = str(input("Quer continuar [S/N]?")).upper()[0]
        if opcao in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if opcao == "N":
        break
print("-="  * 30)
print('cod ',end='')
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 interrompe)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe este jogador {busca}...")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"  No jogo {i + 1} fez {g} gols.")
    print('-' * 40)
print("Volte sempre!")



