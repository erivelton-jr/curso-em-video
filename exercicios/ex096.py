def titulo():
    print('-' * 30)
    print('Calculadora de Areas')
    print('-' * 30)

def area(a, b):
    soma = a * b
    print(f'O terreno de {a} X {b} tem {soma:.1f}m²')


titulo()
a = float(input('Largura do terreno: '))
b = float(input('Comprimento do terreno'))
area(a, b)
