player = {}
gols = []

player['Jogador'] = str(input('Nome: ')).title().strip()
player['Partidas'] = int(input('Partidas jogadas: '))

for gol in range(1, player['Partidas'] + 1):
    gols.append(int(input(f'Numero de gols na partida {gol}')))
    player['Gols'] = gols
player['Total de Gols'] = sum(gols)
print('-' * 30)
print(player)
print('-' * 30)

print(f"O {player['Jogador']} jogou {player['Partidas']} partidas")

for i, v in enumerate(player['Gols']):
    print(f"Na partida {i+1}, o {player['Jogador']} fez {v} gols")
print(f"No total, {player['Jogador']} marcou {player['Total de Gols']} gols")