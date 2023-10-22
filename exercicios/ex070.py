val = maior = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    price = float(input('Valor: '))
    cont += 1
    val += price


    if price > 1000:
        maior += 1
    if cont == 1 or price < menor:
        menor = price
        barato = prod

    print('=' * 30)
    con = str(input('Adicionar mais produtos? [S/N]: ')).upper()
    print('=' * 30)
    if con == 'N':
        break
print(f'Total: {val:.2f}$\n'
      f'Temos {maior} produtos custando mais de 1000.00$\n'
      f'o produto mais barato foi {barato} e custa {menor:.2f}$')