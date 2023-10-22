player = {}
dados = []

while True:
    gol = []
    player['Nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input('Partidas jogadas: '))

    for x in range(1, partidas + 1):
        gol.append(int(input(f'Gols marcados na {x}ª partida')))
    player['Gols'] = gol
    player['Total de Gols'] = sum(gol)
    dados.append(player.copy())
    while True:
        play = str(input('Deseja adicionar mais jogadores? [S/N] ')).upper().strip()
        if play in 'SN':
            break
        print('Erro! Deve ser [S/N]')
    if play == 'N':
        break
print()
print('cod  ', end='')
for l in player.keys():
    print(f'{l:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(dados):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    play = int(input('Mais detalhes de qual jogador? (999 para finalizar)'))
    for k, v in enumerate(dados[play]['Gols']):
        print(f"Na partida {k} o {dados[play]['Nome']} marcou {v} gols")