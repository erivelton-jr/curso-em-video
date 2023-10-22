x = int(input('Primeiro termo: '))
y = int(input('Razão: '))

cont = 1
while cont <= 10:
    print(f'{x}', end='')
    print(' ► ' if cont < 10 else ' pausa ', end='')
    if cont == 10:
        t = int(input('\nQuantos termos você quer ve: '))
        print(f'{x}', end='')
        print(' ► ' if cont < t else ' pausa ', end='')
    cont += 1
    x += y
