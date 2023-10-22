num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
while True:
    x = int(input('Diga um valor: '))
    if 0 <= x <= 20:
        print(f'Você digitou {num[x]}')
    else:
        print('Valor invalido.', end=' ')
    res = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if res == 'N':
        break
