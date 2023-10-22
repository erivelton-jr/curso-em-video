p = ('BANANA', 'PEDAL', 'DICA', 'VITORIA')

for v in p:
    print(f'\nna palavra {v} tem: ', end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')