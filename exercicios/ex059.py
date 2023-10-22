x = float(input('Valor 1: '))
y = float(input('Valor 2: '))
op = 0

while op != 5:
    op = int(input('[1] SOMAR\n'
                   '[2] MULTIPLICAR\n'
                   '[3] MAIOR\n'
                   '[4] NOVOS NUMEROS\n'
                   '[5] SAIR DO PROGRAMA\n'))
    if op == 5:
        print('Finalizando programa...')
    if op == 1:
        print(f'{x} + {y} = {x+y}')
    if op == 2:
        print(f'{x} x {y} = {x*y}')
    if op == 3:
        if x > y:
            print(x)
        elif y > x:
            print(y)
        else:
            print('Os dois valores são iguais')
    elif op == 4:
        x = float(input('Valor 1: '))
        y = float(input('Valor 2: '))

print('programa finalizado')
