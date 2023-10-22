while True:
    n = int(input('Diga um valor: '))
    print('-' * 30)
    if n >= 0:
        for x in range(0, 10):
            print(f'{n} x {x} = {n * x}')
        print('-' * 30)
    else:
        print('\033[0:31mValor invalido.')
        break
print('programa finalizado.')