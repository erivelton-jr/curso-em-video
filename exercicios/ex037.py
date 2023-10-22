n = int(input('Diga um valor: '))
bc = int(input('Qual será a base de conversão? \n'
               '1 - Binario\n'
               '2 - Octadecimal\n'
               '3 - hexadecimal\n'))

if bc == 1:
    print(bin(n)[3:])
elif bc == 2:
    print(oct(n)[3:])
elif bc == 3:
    print(hex(n)[3:])
else:
    print('Numero invalido')
