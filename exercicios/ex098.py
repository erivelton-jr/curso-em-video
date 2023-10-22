from time import sleep

def titulo(x):
    print('-' * (len(x) + 2))
    print(x)
    print('-' * (len(x) + 2))
    sleep(1)

def contador(i, f, p):
    titulo('Contagem de {1} a 10:')
    i=0
    while i < 10:
        i += 1
        print(f'{i} ', end='')
        print('Fim!' if i == 10 else '', end='')
        sleep(1)
    print()

    titulo('De 10 até 0, de 2 em 2')
    f=10
    while f > -2:
        print(f'{f} ', end='')
        print('Fim!' if f == 0 else '', end='')
        f -= 2

    print()

    titulo(f'De {x} até {y}, de {z} em {z}')
    for c in range(x, y + 1, z):
        print(f'{c} ', end='')
        print('Fim' if c == y else '', end='')





