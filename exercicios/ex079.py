n = []
while True:
    num = int(input('Diga um valor: '))
    n.append(num)
    add = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if add == 'N':
        break
n.sort()
res = list(set(n))

print(res)
