n1 = int(input('Diga um numero: '))
n2 = int(input('Diga outro numero: '))
n3 = int(input('Mais um numero: '))
num = [n1, n2, n3]
x = sorted(num, reverse=True)
print(f'O numero maior é: {x[0]}')
print(f'o menor é: {x[2]}')
