print('\033[35mLOJAS PYTHON 3\033[m')
p = float(input('Valor do produto: $'))
pag = str(input('Forma de pagamento:\n'
                '[ 1 ] PIX\n'
                '[ 2 ] Á vista no cartão.\n'
                '[ 3 ] Até 2x no cartão.\n'
                '[ 4 ] 3x ou mais no cartão.\n'))
pix = p - (p * 10 / 100)
card = p - (p * 5 / 100)
cred = (p * 20 / 100) + p

if pag == '1':
    print(f'O produto ficará por {pix:.2f}$ no PIX.')
elif pag == '2':
    print(f'O produto ficará por {card:.2f}$ à vista no cartão.')
elif pag == '3':
    print(f'O produto ficará por {p}$ parcelado em 2x de {p / 2}.')
elif pag == '4':
    par = int(input('Quantas vezes você gosaria de parcelar: '))
    print(f'O produto ficará por {cred}$ dividido em {par}x de {p / par}$.')
else:
    print('Só temos as 4 opções de pagamento')
