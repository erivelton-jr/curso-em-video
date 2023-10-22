from math import hypot
x = float(input('Diga o valor do Cateto Oposto: '))
y = float(input('Diga o valor do Cateto Adjacente: '))
hi = hypot(x, y)
print(f'A hipotenusa é: {hi:.2f}')
