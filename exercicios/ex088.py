from random import sample
from time import sleep

print('-'*30)
print('MEGA DA VIRADA')
print('-' * 30)
x = int(input('Quantos jogos você quer fazer?' ))
jogos = []

for y in range(0, x):
    jogos.append(sample(range(0, 60), 6))
    print(f'jogo {y+1}: {sorted(jogos[y])}')
    sleep(1)
