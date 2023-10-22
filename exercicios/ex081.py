lista = []
while True:
    lista.append(int(input('Diga um valor: ')))
    con = str(input('Deseja continuar? [S/N] ')).strip().upper()

    if con == 'N':
        break

print(f'Foi digitado {len(lista)} elementos')
lista.sort()
print(f'Lista em ordem crescente {lista}')
lista.sort(reverse=True)
print(f'lista em ordem decrescente {lista}')
if 5 in lista:
    print(f'O numero 5 está na lista')
else:
    print('5 não está na lista')