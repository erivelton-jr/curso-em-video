soma = 0
n = 0

for c in range(1, 7):
    x = int(input(f'Digite o {c}º valor:'))

    if x % 2 ==0:
        soma += x
        n += 1
print(f'A soma entre os {c} numeros é igual {soma}')


