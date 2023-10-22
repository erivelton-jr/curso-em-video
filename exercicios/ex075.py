n = (int(input('Primeiro valor: ')),
     int(input('Segundo valor: ')),
     int(input('Terceiro valor: ')),
     int(input('Quarto Valor: ')))
nove = n.count(9)

print(f'Os valores são: {n}')
print(f'Foram digitados {nove} numero 9')
if 3 in n:
    print(f'o numero 3 está na posição {n.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=', ')