p = float(input('Seu Kg: '))
a = float(input('Altura: '))
imc = p / (a ** 2)
print(f'Seu IMC é {imc:.1f}. ', end='')
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
else:
    print(f'Obesidade.')