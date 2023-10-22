from random import randrange
count = 0
while True:
    x = str(input('PAR OU IMPAR [P/I]? ')).upper()
    y = int(input('Diga um valor: '))
    comp = randrange(11)
    val = y + comp
    print('-' * 40)
    print(f'você escolheu {y} e eu {comp}. Totalizando {val}.', end=' ')
    print('Deu par' if (val % 2) == 0 else 'Deu impar')
    print('-' * 40)
    if (val % 2) == 0:
        if x == 'P':
            print('VOCÊ GANHOU!')
            print('-=' * 10)
        else:
            print('EU GANHEI!')
            print('-=' * 10)
            break
    else:
        if x == 'I':
            print('VOCÊ GANHOU!')
            print('-=' * 10)
        else:
            print('EU GANHEI!')
            print('-=' * 10)
            break
    count += 1
print(f'Você ganhou {count} vezes')
