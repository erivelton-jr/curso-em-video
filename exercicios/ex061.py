x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{x}', end='')
    print(' → ' if cont < 10 else ' FIM ', end='')
    cont += 1
    x+= y
