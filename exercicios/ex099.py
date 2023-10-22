from random import randrange
from time import sleep

def maior(c):
    l = []
    if c > 0:
        print(f'Os numeros foram: ', end='')
        for x in range(0, c):
            l.append(randrange(1, 10))
            print(f'{l[x]} ', end=''), sleep(0.5)
        sleep(0.5)
        print(f'Ao todo foi analisado {len(l)} numeros')
        sleep(0.5)
        print(f'O maior numero é {max(l)}')
        print('=-' * 30)
    else:
        l.append(0)
        print(f'Ao todo foi analisado {len(l) - 1} numeros')
        print(f'O maior numero é {max(l)}')


maior(6)
maior(3)
maior(0)