a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))

if a > b:
    print(f'O numero {a} é maior que o {b}.')
elif b > a:
    print(f'O numero {b} é a maior que o {a}.')
else:
    print('Ambos são iguais.')