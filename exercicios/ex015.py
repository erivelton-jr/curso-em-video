d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input(f'Quantos KM foram percorrido?'))
v = (d * 60) + (km * 0.15)
print(f'O aluguel do carro custou: {v:.2f}R$')
