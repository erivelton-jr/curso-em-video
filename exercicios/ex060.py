from math import factorial
'''f = int(input(f'fatorial de: '))
c = f
print(f'{f}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c-= 1


print(factorial(f))'''

f = int(input(f'fatorial de: '))
print(f'{f}! = ', end='')
for x in range(f, 0, -1):
    print(f'{x}', end='')
    print(' = ' if x == 1 else ' x ', end='')
print(factorial(f))