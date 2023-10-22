from time import sleep
from random import randrange, randint

jogadores = dict()
c = 1
print('VAMOS COMEÇAR...'), sleep(2)
print('=' * 30)

for dado in range(1, 5):
    jogadores[f'jogador {dado}'] = randint(1, 7)
    print(f'Vez do jogador {dado}...'), sleep(2)
    print('-' * 25)

for k, v in jogadores.items():
    print(f'{k} jogou o numero: {v}')

print('=' * 15)
print('RESULTADO')
print('=' * 15)

ranking = sorted(jogadores.items(), key=lambda x:x[1], reverse=True)
val = dict(ranking)

for k, v in val.items():
    print(f'{c}º lugar = {k} ({v})'), sleep(1)
    c += 1