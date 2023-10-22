count = soma = s = 0
lista = []
while s != 'n':
    val = int(input('Diga um valor: '))
    count += 1
    lista += [val]
    lista.sort()
    soma += val
    s = str(input('Deseja continuar? [S/N]: ')).lower().strip()

print(f'foi digitado {count} numeros.\n'
      f'a média entre eles são {soma / count:.2f}.\n'
      f'o maior valor é {lista[-1]}')
