num = [[], []]

for x in range(1, 8):
    val = int(input(f'Diga o {x}º valor: '))
    if val % 2 == 0:
        num[0].append(val)
        if val == 0:
            num[0].remove(0)
    else:
        num[1].append(val)
print(f'Os valores da lista foi: {num}')
print(f'Os valores pares da lista são: {sorted(num[0])}')
print(f'Os valores impares da lista são: {sorted(num[1])}')