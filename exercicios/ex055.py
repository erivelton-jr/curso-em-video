lista = []
for x in range(1, 6):
    p = float(input(f'peso da {x}ª pessoa: '))
    lista += [p]
    lista.sort()


print(f'o maior peso foi {lista[-1]}kg.\n'
      f'o menor foi {lista[0]}kg.')