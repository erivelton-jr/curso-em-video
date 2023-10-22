saque = int(input('Valor de saque: '))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Vão ser necessario {totalced} notas de {ced}$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        totalced = 0
        if total == 0:
            break
