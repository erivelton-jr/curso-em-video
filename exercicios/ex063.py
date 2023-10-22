n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
cont = 3
print(f'{n1}, {n2}, ', end='')

while cont <= n:
    n3 = n1 + n2
    print(f' {n3}, ', end='')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
