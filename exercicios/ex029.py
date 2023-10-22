km = int(input('Quantos Km/h o carro percorreu? '))
if km > 80:
    print(f'Você excedeu o limite de velocidade.')
    print(f'Valor a pagar é de {(km-80)*7.0}')
else:
    print('Você não foi multado.')
