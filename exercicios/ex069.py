maior = h = m = 0

while True:
    print('-' * 30)
    print('CADASTRE DE PESSOAS')
    print('-' * 30)

    id = int(input('Idade: '))
    s = ' '
    p = ' '

    while s not in "MF":
        s = str(input('Sexo [M/F]: ')).strip().upper()

    if id > 17:
        maior += 1
    if s == 'M':
        h += 1
    if s == 'F':
        m += 1
        print('-' * 30)

    while p not in "SN":
        p = str(input('Deseja adicionar mais pessoas [S/N]?')).upper()
    if p == 'N':
        break

print('-' * 30)
print(f'tem {maior} pessoas maior de idade')
print(f'Tem {h} homens')
print(f'Tem {m} mulheres.')
