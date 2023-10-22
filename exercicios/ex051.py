print('=' * 30)
print('PROGRSSÃO ARITMETICA')
print('=' * 30)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = a1 + r          #10 termo x = a1 + (10 - 1) * r

for pa in range(a1, (x + 1) * 4, r):
    print(f'{pa}', end=' → ')
