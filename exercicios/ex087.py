matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x][y] = int(input(f'Valor na posição [{x},{y}]: '))

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}]', end='')
        if matriz[x][y] % 2 == 0:
            par += matriz[x][y]
    print()

print(f'A soma dos valores par da matriz é {par}')

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma entre os valores da terceira coluna é {soma}')

if matriz[0][1] > matriz[1][1] or matriz[0][1] > matriz[2][1]:
    print(f'a maior mattriz da segunda coluna é {matriz[0][1]}')
elif matriz[1][1] > matriz[0][1] or matriz[1][1] > matriz[2][1]:
    print(f'A maior matriz da segunda coluna é {matriz[1][1]}')
else:
    print(f'A maior matriz da segunda coluna é {matriz[2][1]}')
