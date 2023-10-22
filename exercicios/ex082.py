listapar = []
listaimpar = []
lista = []
while True:
    num = int(input('Diga um valor: '))
    lista += [num]
    if (num % 2) == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    add = str(input('Deseja adicionar mais um valor? [S/N] ')).strip()
    if add in 'Nn':
        break
listapar.remove(0)
print(lista)
print(f'Os valores pares da lista são {listapar}')
print(f'Os valores impares da lista são {listaimpar}')